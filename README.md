# DriftSiren — Real‑Time Data Drift & Data Quality Monitoring Platform

A production‑style, full‑stack platform to **detect data drift**, **monitor data quality**, and **alert in real time**.
Built to look complex yet remain **runnable end‑to‑end** with Docker. Includes modern tooling recruiters love:
**Next.js + Tailwind**, **FastAPI**, **PostgreSQL**, **Redis + Celery**, **WebSockets**, **Kubernetes manifests**, **CI/CD with GitHub Actions**.

## ✨ Key Features
- Agent SDK sends datasets/events to the backend securely.
- Real‑time drift metrics (PSI, KS, Chi‑Squared) computed in background jobs.
- Live alert stream via WebSocket; historical metrics stored in Postgres.
- Clean dashboard with charts (Recharts) and filters.
- Role‑based users (stub/JWT) and organizations (demo scope).
- Docker Compose one‑command startup. K8s manifests included for cluster deployments.

## 🗂 Project Structure
```
DriftSiren/
  backend/
    app/
      __init__.py
      main.py                # FastAPI app, routes, WebSocket, startup DB init
      config.py
      db.py
      models.py
      schemas.py
      auth.py
      routers/
        __init__.py
        health.py
        ingest.py
        metrics.py
        alerts.py
      ws_manager.py
      celery_app/
        __init__.py
        app.py               # Celery worker and periodic tasks
      ml/
        __init__.py
        drift.py             # PSI, KS, Chi-Squared implementations
        utils.py
      tests/
        test_drift.py        # Unit tests for metrics
    Dockerfile
    requirements.txt
  agent/
    ds_agent/
      __init__.py
      client.py              # CLI to send CSV/JSON rows to backend
    setup.py
    README.md
  frontend/
    app/
      globals.css
      layout.tsx
      page.tsx
      alerts/page.tsx
      metrics/page.tsx
      orgs/page.tsx
      components/
        Card.tsx
        Chart.tsx
        Header.tsx
        Table.tsx
        StatusDot.tsx
      lib/ws.ts
      lib/api.ts
    public/
      logo.svg
    package.json
    tsconfig.json
    next.config.mjs
    postcss.config.mjs
    tailwind.config.ts
    Dockerfile
  k8s/
    namespace.yaml
    postgres.yaml
    redis.yaml
    backend.yaml
    frontend.yaml
    worker.yaml
    configmap.yaml
  .github/workflows/
    ci.yml
  docker-compose.yml
  .env.example
  README.md
```

## 🚀 Quick Start (Docker)
1. Clone the repo and create `.env` from `.env.example`.
2. Run: `docker compose up --build`.
3. Open **http://localhost:3000** (frontend) and **http://localhost:8000/docs** (backend API).

> Demo creds: any email works; click "Sign In (Demo)" to get a JWT.

## 🧪 Sample Run (without Docker)
- Backend: `cd backend && uvicorn app.main:app --reload`
- Worker: `cd backend && celery -A app.celery_app.app worker --loglevel=INFO`
- Frontend: `cd frontend && npm i && npm run dev`

## 🔒 Security Notes
This is a demo. Replace `SECRET_KEY`, add proper auth, HTTPS, and harden CORS before production.

## 🧰 Tech Highlights (Recruiter‑friendly)
Next.js 14, TypeScript, Tailwind, Recharts • FastAPI, Pydantic v2 • SQLAlchemy 2.0 • Celery/Redis • PostgreSQL 16 • WebSockets • Docker & K8s • GitHub Actions CI

## 📄 License
MIT
