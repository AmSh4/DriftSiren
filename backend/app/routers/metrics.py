from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..db import get_db
from .. import models, schemas

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("/", response_model=list[schemas.MetricOut])
def list_metrics(dataset_id: int | None = None, db: Session = Depends(get_db)):
    stmt = select(models.Metric).order_by(models.Metric.created_at.desc()).limit(200)
    if dataset_id:
        stmt = stmt.where(models.Metric.dataset_id == dataset_id)
    return db.execute(stmt).scalars().all()
