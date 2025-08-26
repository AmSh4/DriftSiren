from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .db import Base, engine, SessionLocal
from . import models
from .routers import health, ingest, metrics, alerts
from .auth import demo_token
from .ws_manager import manager

app = FastAPI(title="DriftSiren API")

origins = [o.strip() for o in settings.CORS_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    # Ensure a demo org and dataset exist
    db = SessionLocal()
    try:
        org = db.query(models.Organization).first()
        if not org:
            org = models.Organization(name="DemoOrg"); db.add(org); db.commit(); db.refresh(org)
            user = models.User(email="demo@demo", org_id=org.id, role="admin")
            ds = models.Dataset(org_id=org.id, name="demo_dataset", schema={"x":"number","y":"number"})
            db.add_all([user, ds]); db.commit()
    finally:
        db.close()

app.include_router(health.router)
app.include_router(ingest.router)
app.include_router(metrics.router)
app.include_router(alerts.router)

@app.get("/demo/signin")
def demo_signin(email: str = "demo@demo"):
    return {"token": demo_token(email)}

@app.websocket("/ws/alerts")
async def ws_alerts(ws: WebSocket):
    await manager.connect(ws)
    try:
        while True:
            await ws.receive_text()  # keepalive
    except WebSocketDisconnect:
        manager.disconnect(ws)
