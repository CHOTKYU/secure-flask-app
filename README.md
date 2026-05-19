# Secure Flask App — DevSecOps Project

Практичний DevSecOps проект — захищений веб-додаток на Flask з автоматичним security pipeline через GitHub Actions.

## Про проект

Простий REST API на Python/Flask розгорнутий в Docker контейнері з повним DevSecOps pipeline який автоматично запускається на кожен `git push`.

## Архітектура

Developer
↓
git push
↓
GitHub Actions Pipeline
├── Gitleaks    → сканування секретів
├── Checkov     → сканування Dockerfile
├── Docker Build → збірка образу
└── Trivy       → сканування CVE вразливостей
↓
✅ Результат видно в GitHub Actions

## Endpoints

| Метод | URL | Опис |
|---|---|---|
| GET | / | Головна сторінка — статус додатку |
| GET | /health | Health check endpoint |

## Security практики

### 1. Non-root container
Додаток запускається від непривілейованого користувача `appuser` а не від `root`. Це обмежує можливий збиток у разі компрометації контейнера.

### 2. Gitleaks — Secret Detection
Автоматично сканує весь код і git історію на наявність:
- API ключів
- Паролів
- Токенів
- Private keys

### 3. Checkov — IaC Security
Перевіряє Dockerfile на відповідність security best practices:
- Чи використовується non-root user
- Чи є зайві привілеї
- Чи правильно налаштований образ

### 4. Trivy — CVE Scanning
Сканує Docker образ на відомі вразливості (CVE) з рівнем HIGH та CRITICAL. База даних вразливостей оновлюється автоматично.

## GitHub Actions Pipeline

Pipeline запускається автоматично на кожен `push` або `pull request` в гілку `main`:

```yaml
git push → Gitleaks → Checkov → Build → Trivy → ✅/❌
```

Час виконання: ~1-2 хвилини

## Стек технологій

| Технологія | Версія | Призначення |
|---|---|---|
| Python | 3.11 | Мова програмування |
| Flask | 3.0.0 | Веб-фреймворк |
| Docker | latest | Контейнеризація |
| GitHub Actions | - | CI/CD pipeline |
| Gitleaks | v2 | Secret scanning |
| Checkov | latest | IaC scanning |
| Trivy | latest | CVE scanning |

## Запуск локально

```bash
# Клонувати репозиторій
git clone https://github.com/CHOTKYU/secure-flask-app.git
cd secure-flask-app

# Запустити через Docker
docker compose up --build

# Перевірити
curl http://localhost:5000
curl http://localhost:5000/health
```

## Структура проекту## Endpoints

| Метод | URL | Опис |
|---|---|---|
| GET | / | Головна сторінка — статус додатку |
| GET | /health | Health check endpoint |

## Security практики

### 1. Non-root container
Додаток запускається від непривілейованого користувача `appuser` а не від `root`. Це обмежує можливий збиток у разі компрометації контейнера.

### 2. Gitleaks — Secret Detection
Автоматично сканує весь код і git історію на наявність:
- API ключів
- Паролів
- Токенів
- Private keys

### 3. Checkov — IaC Security
Перевіряє Dockerfile на відповідність security best practices:
- Чи використовується non-root user
- Чи є зайві привілеї
- Чи правильно налаштований образ

### 4. Trivy — CVE Scanning
Сканує Docker образ на відомі вразливості (CVE) з рівнем HIGH та CRITICAL. База даних вразливостей оновлюється автоматично.

## GitHub Actions Pipeline

Pipeline запускається автоматично на кожен `push` або `pull request` в гілку `main`:

```yaml
git push → Gitleaks → Checkov → Build → Trivy → ✅/❌
```

Час виконання: ~1-2 хвилини

## Стек технологій

| Технологія | Версія | Призначення |
|---|---|---|
| Python | 3.11 | Мова програмування |
| Flask | 3.0.0 | Веб-фреймворк |
| Docker | latest | Контейнеризація |
| GitHub Actions | - | CI/CD pipeline |
| Gitleaks | v2 | Secret scanning |
| Checkov | latest | IaC scanning |
| Trivy | latest | CVE scanning |

## Запуск локально

```bash
# Клонувати репозиторій
git clone https://github.com/CHOTKYU/secure-flask-app.git
cd secure-flask-app

# Запустити через Docker
docker compose up --build

# Перевірити
curl http://localhost:5000
curl http://localhost:5000/health
```

## Структура проекту
secure-flask-app/
├── app/
│   ├── app.py              ← Flask додаток
│   └── requirements.txt    ← Python залежності
├── Dockerfile              ← non-root, slim образ
├── docker-compose.yml      ← локальний запуск
├── .github/
│   └── workflows/
│       └── security.yml    ← GitHub Actions pipeline
└── README.md
