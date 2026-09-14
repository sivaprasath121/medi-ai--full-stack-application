# VPS deployment runbook

## Goal
Deploy the MediAI backend on a Linux VPS with Docker, Postgres, and reverse-proxy TLS termination.

## Prerequisites
- Ubuntu/Debian VPS
- Docker Engine installed
- Nginx or Caddy installed
- A domain name or public IP
- Postgres database available or a local containerized Postgres

## 1) Prepare the server
Install required packages:
```bash
sudo apt update
sudo apt install docker.io docker-compose-plugin nginx certbot python3-certbot-nginx -y
```

## 2) Copy project files
```bash
scp -r /path/to/MediAI user@server:/srv/medi-ai
```

## 3) Configure environment
Create a production `.env` file:
```bash
cp .env.production.example .env
```
Then set the real values for:
- DATABASE_URL
- JWT_SECRET
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD

## 4) Run the stack
```bash
docker compose -f deploy/docker-compose.production.yml up -d --build
```

## 5) Configure reverse proxy
Use [deploy/vps-nginx.conf](../deploy/vps-nginx.conf) as a base template.
- Replace the domain name with your own
- Point Nginx to localhost:8000

## 6) Enable HTTPS
```bash
sudo certbot --nginx -d your-domain.example.com
```

## 7) Validation
```bash
curl https://your-domain.example.com/health
```

Expected:
```json
{"status":"ok","service":"MediAI"}
```

## 8) Operational checklist
- Keep `.env` file permissions tight
- Review Docker logs and restart policies
- Enable firewall rules
- Back up the database regularly
- Monitor uptime and SSL expiration
