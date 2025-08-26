# Folder Structure

        DriftSiren/
        │
        ├── backend/
        │   ├── app/
        │   │   ├── __init__.py
        │   │   ├── main.py                # FastAPI app, routes, WebSocket, startup DB init
        │   │   ├── config.py
        │   │   ├── db.py
        │   │   ├── models.py
        │   │   ├── schemas.py
        │   │   ├── auth.py
        │   │   ├── routers/
        │   │   │   ├── __init__.py
        │   │   │   ├── health.py
        │   │   │   ├── ingest.py
        │   │   │   ├── metrics.py
        │   │   │   └── alerts.py
        │   │   ├── ws_manager.py
        │   │   ├── celery_app/
        │   │   │   ├── __init__.py
        │   │   │   └── app.py             # Celery worker and periodic tasks
        │   │   ├── ml/
        │   │   │   ├── __init__.py
        │   │   │   ├── drift.py           # PSI, KS, Chi-Squared implementations
        │   │   │   └── utils.py
        │   │   └── tests/
        │   │       └── test_drift.py      # Unit tests for metrics
        │   ├── Dockerfile
        │   └── requirements.txt
        │
        ├── agent/
        │   ├── ds_agent/
        │   │   ├── __init__.py
        │   │   └── client.py              # CLI to send CSV/JSON rows to backend
        │   ├── setup.py
        │   └── README.md
        │
        ├── frontend/
        │   ├── app/
        │   │   ├── globals.css
        │   │   ├── layout.tsx
        │   │   ├── page.tsx
        │   │   ├── alerts/page.tsx
        │   │   ├── metrics/page.tsx
        │   │   ├── orgs/page.tsx
        │   │   ├── components/
        │   │   │   ├── Card.tsx
        │   │   │   ├── Chart.tsx
        │   │   │   ├── Header.tsx
        │   │   │   ├── Table.tsx
        │   │   │   └── StatusDot.tsx
        │   │   ├── lib/ws.ts
        │   │   └── lib/api.ts
        │   ├── public/
        │   │   └── logo.svg
        │   ├── package.json
        │   ├── tsconfig.json
        │   ├── next.config.mjs
        │   ├── postcss.config.mjs
        │   ├── tailwind.config.ts
        │   └── Dockerfile
        │
        ├── k8s/
        │   ├── namespace.yaml
        │   ├── postgres.yaml
        │   ├── redis.yaml
        │   ├── backend.yaml
        │   ├── frontend.yaml
        │   ├── worker.yaml
        │   └── configmap.yaml
        │
        ├── .github/
        │   └── workflows/
        │       └── ci.yml
        │
        ├── docker-compose.yml
        ├── .env.example
        ├── structure/
            └── README.md
        └── README.md
