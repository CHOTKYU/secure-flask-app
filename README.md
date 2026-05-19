Практичний DevSecOps проект — захищений веб-додаток на Flask з автоматичним security pipeline через GitHub Actions.

## Про проект

Простий REST API на Python/Flask розгорнутий в Docker контейнері з повним DevSecOps pipeline який автоматично запускається на кожен git push.

## Архітектура
git push → Gitleaks → Checkov → Docker Build → Trivy → результат
## Endpoints

| Метод | URL | Опис |
|---|---|---|
| GET | / | Статус додатку |
| GET | /health | Health check |

## Security практики

- **Non-root container** — запускається від appuser а не root
- **Gitleaks** — сканує секрети в коді
- **Checkov** — перевіряє Dockerfile
- **Trivy** — сканує CVE вразливості HIGH/CRITICAL

## Стек

| Технологія | Призначення |
|---|---|
| Python 3.11 + Flask | Веб-додаток |
| Docker | Контейнеризація |
| GitHub Actions | CI/CD pipeline |
| Gitleaks | Secret scanning |
| Checkov | IaC scanning |
| Trivy | CVE scanning |

## Запуск локально

```bash
git clone https://github.com/CHOTKYU/secure-flask-app.git
cd secure-flask-app
docker compose up --build
```
