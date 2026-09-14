# Render deployment runbook

## Goal
Deploy the MediAI backend to Render with secure environment variables and a managed Postgres database.

## Prerequisites
- Render account
- GitHub repository connected to Render
- Managed Postgres database provisioned in Render

## 1) Create the service
- Go to Render Dashboard
- Click New -> Web Service
- Connect the GitHub repository
- Select the repository root
- Choose Python environment

## 2) Configure build and start commands
Build command:
```bash
cd backend && pip install -r requirements.txt
```

Start command:
```bash
cd backend && uvicorn app.main:app --host 0.0.0.0 --port 10000
```

## 3) Set environment variables
Set these in the Render dashboard:
- APP_NAME=MediAI
- ENVIRONMENT=production
- DATABASE_URL=<render-postgres-connection-string>
- JWT_SECRET=<long-random-secret>
- JWT_ALGORITHM=HS256
- AI_MODE=mock

## 4) Connect Postgres
- Create Postgres database on Render
- Copy the internal or external connection URL
- Paste it into DATABASE_URL

## 5) Deploy
- Click Create Web Service
- Render builds and starts the app
- Confirm health endpoint responds on `/health`

## 6) Validation
Run:
```bash
curl https://<your-render-url>/health
```

Expected:
```json
{"status":"ok","service":"MediAI"}
```

## 7) Operational checklist
- Rotate JWT_SECRET quarterly
- Keep DATABASE_URL in Render secrets
- Monitor logs and app health
- Run smoke tests in CI before release
