from celery import Celery
from ..config import settings
from ..db import SessionLocal, engine, Base
from .. import models
from datetime import datetime, timedelta
from ..ml.drift import compute_psi, compute_ks, compute_chi2
from sqlalchemy import select, func
import json
from ..ws_manager import manager

app = Celery("driftsiren", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

def init_db():
    Base.metadata.create_all(bind=engine)

@app.task
def enqueue_compute_metrics(dataset_id: int):
    init_db()
    db = SessionLocal()
    try:
        # Use last N=200 events as "current window", previous N=200 as "baseline"
        def fetch_events(offset: int):
            stmt = (
                select(models.IngestEvent)
                .where(models.IngestEvent.dataset_id == dataset_id)
                .order_by(models.IngestEvent.created_at.desc())
                .offset(offset)
                .limit(200)
            )
            return [e.payload for e in db.execute(stmt).scalars().all()]

        current = fetch_events(0)
        baseline = fetch_events(200)
        if len(current) < 20 or len(baseline) < 20:
            return "not_enough_data"

        psi = compute_psi(baseline, current)
        ks = compute_ks(baseline, current)
        chi2 = compute_chi2(baseline, current)

        now = datetime.utcnow()
        met = models.Metric(
            dataset_id=dataset_id,
            window_start=now - timedelta(minutes=5),
            window_end=now,
            psi=psi,
            ks=ks,
            chi2=chi2,
            details=json.dumps({"n_baseline": len(baseline), "n_current": len(current)}),
        )
        db.add(met)
        db.commit()
        db.refresh(met)

        # Simple alerting
        if psi > 0.2 or ks > 0.2:
            al = models.Alert(dataset_id=dataset_id, severity="HIGH", message=f"Drift detected (PSI={psi:.3f}, KS={ks:.3f})")
            db.add(al); db.commit()
            # WebSocket broadcast
            import asyncio
            msg = json.dumps({"type":"alert","dataset_id":dataset_id,"psi":psi,"ks":ks,"id":al.id})
            try:
                asyncio.get_event_loop().create_task(manager.broadcast(msg))
            except RuntimeError:
                # not in event loop (worker), ignore silently
                pass

        return "ok"
    finally:
        db.close()
