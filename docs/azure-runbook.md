# Azure App Service deployment runbook

## Goal
Deploy the MediAI backend to Azure App Service with managed Postgres and secret-based configuration.

## Prerequisites
- Azure subscription
- Resource group created
- App Service plan created
- PostgreSQL database available

## 1) Create the app service
- In Azure Portal, create a Web App
- Choose Python 3.12
- Use Linux or Windows depending on your preference

## 2) Configure deployment source
- Use GitHub Actions or Azure deployment center
- Point to this repository

## 3) Set App Settings
Configure these under Configuration -> Application settings:
- APP_NAME=MediAI
- ENVIRONMENT=production
- DATABASE_URL=<azure-postgres-connection-string>
- JWT_SECRET=<secure-random-secret>
- JWT_ALGORITHM=HS256
- AI_MODE=mock

## 4) Optional: Key Vault integration
- Store JWT_SECRET and DB credentials in Azure Key Vault
- Reference them as App Settings or managed identities

## 5) Deploy
- Push code to GitHub or trigger deployment from Azure
- Confirm app starts successfully

## 6) Validation
In the browser or with curl:
```bash
curl https://<your-app-name>.azurewebsites.net/health
```

Expected:
```json
{"status":"ok","service":"MediAI"}
```

## 7) Operational checklist
- Use diagnostics logs
- Monitor resource metrics and scale rules
- Keep secrets in Key Vault
- Review health and failures frequently
