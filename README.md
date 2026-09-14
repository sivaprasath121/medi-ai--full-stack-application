# MediAI

MediAI is a modern healthcare platform demo built with a React frontend and a FastAPI backend. This repository is structured to support the full hospital SaaS experience described in the project brief, with Phase 1 focused on the working foundation: project scaffolding, frontend shell, backend API, and PostgreSQL-ready configuration.

## Phase 1 delivered

- React + TypeScript frontend scaffold with Vite
- FastAPI backend with health endpoints
- PostgreSQL service configuration via Docker Compose
- Environment configuration template
- Basic project structure for subsequent healthcare modules

## Folder structure

```text
MediAI/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── .venv/
```

## Run locally

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Docker Compose

```bash
docker compose up --build
```

## Production hardening baseline

This project now supports a deployment-safe baseline with:
- SQLite default for local development and test runs
- Postgres-ready `DATABASE_URL` configuration for real deployments
- environment-based secrets via `.env` files and platform secret stores
- production-friendly Docker settings with `restart: unless-stopped`
- smoke-test automation in the repository

## Smoke validation

Run the smoke suite from the project root:

```bash
python scripts/smoke_test.py
```

or directly:

```bash
cd backend && python -m pytest tests/test_smoke.py -q
```

This validates the critical app flows:
- health and root endpoints
- patient login and role flow
- patient lookup flow
- doctor overview and patient queue
- appointment scheduling
- medical record retrieval

## Production deployment checklist

### 1) Real Postgres-backed persistence
- Set `DATABASE_URL` to a managed Postgres instance such as Neon, Supabase, Azure Database for PostgreSQL, or a VM-hosted Postgres.
- Keep `sqlite:///./medi_ai.db` only for local dev and CI smoke runs.

### 2) Secure env / secret handling
- Copy `.env.example` to `.env` locally.
- For production, inject secrets through Render, Azure App Service, Railway, or a secrets manager.
- Never commit `JWT_SECRET`, `POSTGRES_PASSWORD`, or API keys to Git.

### 3) Production Docker settings
- Use `docker compose` for local orchestration.
- For production deployments, prefer a managed runtime and keep `restart: unless-stopped` plus health checks enabled.
- Build images with minimal dependencies and no local dev artifacts.

### 4) Smoke-test automation
- Run `python scripts/smoke_test.py` before release.
- Add this to your CI pipeline and deployment gate.

### 5) Deployment targets
#### Render
- Service type: Web Service
- Build command: `cd backend && pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
- Add environment variables: `DATABASE_URL`, `JWT_SECRET`, `ENVIRONMENT=production`

#### Azure App Service
- Deploy the backend container or Python app directly.
- Configure App Settings with the same env vars listed above.
- Use managed Postgres or Azure Database for PostgreSQL.

#### Railway
- Deploy the backend service and attach a Postgres database.
- Set `DATABASE_URL` from the Railway-provided Postgres addon.
- Ensure host, port, and credentials are injected as runtime variables.

#### VPS / self-hosted
- Install Docker or systemd service for the backend.
- Expose port 8000 behind a reverse proxy such as Nginx or Caddy.
- Use TLS termination and a secret store like Docker secrets or a `.env` file with restricted permissions.

## Operational next steps

- Add real database migrations with Alembic.
- Replace in-memory patient/doctor data with persisted models.
- Add authentication middleware enforcement for protected routes.
- Add structured logs and health monitoring.
- Add a GitHub Actions or GitLab CI pipeline to run smoke-tests on every merge.

## QA checklist

- Open the app and switch between patient and doctor views.
- Log in as a patient and confirm the dashboard loads.
- Open the appointment scheduler and create a booking.
- Confirm the doctor queue and medical records render correctly.
- Run the frontend build to confirm the app still compiles.

## Notes

- Default AI mode is intentionally set to mock mode.
- No real secrets or credentials are committed to the repository.
- Demo data is synthetic and intended for local development only.
