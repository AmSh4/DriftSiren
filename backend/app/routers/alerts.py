from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..db import get_db
from .. import models, schemas

router = APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("/", response_model=list[schemas.AlertOut])
def list_alerts(dataset_id: int | None = None, db: Session = Depends(get_db)):
    stmt = select(models.Alert).order_by(models.Alert.created_at.desc()).limit(200)
    if dataset_id:
        stmt = stmt.where(models.Alert.dataset_id == dataset_id)
    return db.execute(stmt).scalars().all()
