from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
from datetime import datetime

class OrgCreate(BaseModel):
    name: str

class OrgOut(BaseModel):
    id: int
    name: str
    created_at: datetime
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    org_id: int

class UserOut(BaseModel):
    id: int
    email: str
    org_id: int
    role: str
    created_at: datetime
    class Config:
        from_attributes = True

class DatasetCreate(BaseModel):
    org_id: int
    name: str
    schema: Dict[str, str]

class DatasetOut(BaseModel):
    id: int
    org_id: int
    name: str
    schema: Dict[str, str]
    created_at: datetime
    class Config:
        from_attributes = True

class IngestEventIn(BaseModel):
    dataset_id: int
    payload: Dict[str, Any]

class MetricOut(BaseModel):
    id: int
    dataset_id: int
    window_start: datetime
    window_end: datetime
    psi: float
    ks: float
    chi2: float
    details: str
    created_at: datetime
    class Config:
        from_attributes = True

class AlertOut(BaseModel):
    id: int
    dataset_id: int
    severity: str
    message: str
    created_at: datetime
    class Config:
        from_attributes = True
