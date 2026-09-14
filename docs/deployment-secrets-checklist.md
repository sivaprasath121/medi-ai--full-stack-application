# Deployment secrets checklist

## Required for every environment

- APP_NAME
- ENVIRONMENT
- DATABASE_URL
- JWT_SECRET
- JWT_ALGORITHM
- AI_MODE

## Render

- Set in the Render dashboard under Environment Variables
- `DATABASE_URL` should point to the managed Postgres instance
- `JWT_SECRET` must be long and random
- Keep `ENVIRONMENT=production`
- Configure health check endpoint `/health`

## Azure App Service

- Add them under App Service -> Configuration -> Application settings
- Use Azure Key Vault for production secret storage when possible
- Required secrets:
  - `DATABASE_URL`
  - `JWT_SECRET`
  - `APP_NAME`
  - `ENVIRONMENT`

## Railway

- Add them under Variables in the Railway project dashboard
- Attach a Postgres database and copy the connection string to `DATABASE_URL`
- Keep `JWT_SECRET` and runtime environment variables private

## VPS / self-hosted

- Use a `.env.production` file with restricted permissions (`chmod 600`)
- Prefer Docker secrets or a managed secret store if available
- Ensure the file is outside the Git repo
- Protect TLS and reverse proxy configuration

## General rules

- Never commit real secrets to Git
- Use different secrets per environment
- Rotate secrets regularly
- Validate runtime environment variables after deployment
