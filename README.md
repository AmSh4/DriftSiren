# DriftSiren  
### `Real‑Time Data Drift & Data Quality Monitoring Platform`

A production‑style, full‑stack platform to **detect data drift**, **monitor data quality**, and **alert in real time**.

## Key Features
- Agent SDK sends datasets/events to the backend securely.
- Real‑time drift metrics (PSI, KS, Chi‑Squared) computed in background jobs.
- Live alert stream via WebSocket; historical metrics stored in Postgres.
- Clean dashboard with charts (Recharts) and filters.
- Role‑based users (stub/JWT) and organizations (demo scope).
- Docker Compose one‑command startup. K8s manifests included for cluster deployments.

## Project Structure  
- https://github.com/AmSh4/DriftSiren/tree/main/Structure
##  Quick Start (Docker)
1. Clone the repo and create `.env` from `.env.example`.
2. Run: `docker compose up --build`.
3. Open **http://localhost:3000** (frontend) and **http://localhost:8000/docs** (backend API).

> Demo creds: any email works; click "Sign In (Demo)" to get a JWT.

## Sample Run (without Docker)
- Backend: `cd backend && uvicorn app.main:app --reload`
- Worker: `cd backend && celery -A app.celery_app.app worker --loglevel=INFO`
- Frontend: `cd frontend && npm i && npm run dev`

## Security Notes
Replace `SECRET_KEY`, add proper auth, HTTPS, and harden CORS before production.

