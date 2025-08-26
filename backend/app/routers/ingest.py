from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from .. import models, schemas
from ..celery_app.app import enqueue_compute_metrics

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/event")
def ingest_event(ev: schemas.IngestEventIn, db: Session = Depends(get_db)):
    ds = db.get(models.Dataset, ev.dataset_id)
    if not ds:
        raise HTTPException(status_code=404, detail="dataset not found")
    rec = models.IngestEvent(dataset_id=ev.dataset_id, payload=ev.payload)
    db.add(rec)
    db.commit()
    db.refresh(rec)
    enqueue_compute_metrics.delay(ev.dataset_id)
    return {"id": rec.id, "status": "accepted"}
