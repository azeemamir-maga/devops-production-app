# DevOps Production App

A production-style Flask web application deployed with Docker, PostgreSQL, and Nginx, featuring automated testing and CI/CD-driven Docker image publishing through GitHub Actions.

This project demonstrates a complete, practical DevOps workflow: containerizing a Python web application, connecting it to a PostgreSQL database, placing Nginx in front of it as a reverse proxy, persisting database data with Docker volumes, running automated tests, hardening the container, optimizing the Docker image, and publishing the final image to Docker Hub through a CI/CD pipeline.

---

## Table of Contents

- [Architecture](#architecture)
- [CI/CD Workflow](#cicd-workflow)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Docker Hub Image](#docker-hub-image)
- [Testing](#testing)
- [Health Check](#health-check)
- [Database](#database)
- [Nginx](#nginx)
- [Security](#security)
- [Useful Docker Commands](#useful-docker-commands)
- [DevOps Concepts Demonstrated](#devops-concepts-demonstrated)
- [Project Goal](#project-goal)
- [Author](#author)
- [License](#license)

---

## Architecture

```text
                         USER
                           |
                           v
                     NGINX :80
                           |
                           v
                    FLASK WEB :5000
                           |
                           v
                    POSTGRESQL :5432
                           |
                           v
                    postgres_data
                    (named volume)
```

**Request flow:** `Client → Nginx :80 → Flask :5000 → PostgreSQL :5432 → Persistent Volume`

The Flask application is never exposed directly to the host. Nginx is the only public HTTP entry point and forwards requests to Flask internally.

---

## CI/CD Workflow

```text
Developer
    |
    v
Git Push
    |
    v
GitHub Actions
    |
    +--> Install Dependencies
    +--> Start PostgreSQL Service
    +--> Run Database Migrations
    +--> Run Pytest
    +--> Build Docker Image
    +--> Authenticate with Docker Hub
    +--> Push Docker Image
    |
    v
Docker Hub
    |
    v
Docker Compose
    |
    +--> Nginx
    +--> Flask
    +--> PostgreSQL
```

The pipeline runs on every push to `master` and on every pull request targeting `master`.

---

## Tech Stack

| Category         | Tools |
|-------------------|-------|
| Language / Framework | Python 3, Flask |
| Database           | PostgreSQL 16, SQLAlchemy, Flask-Migrate |
| Containerization   | Docker, Docker Compose |
| Web Server / Proxy | Nginx |
| CI/CD              | GitHub Actions, Docker Hub |
| Testing            | Pytest |
| Version Control     | Git, GitHub |
| OS                 | Linux / Ubuntu |

---

## Features

- Flask application factory pattern
- PostgreSQL database integration
- CRUD API
- Database migrations with Flask-Migrate
- Dockerized Flask application
- Multi-container architecture via Docker Compose
- Nginx reverse proxy
- Application health endpoint
- Persistent PostgreSQL storage via named volume
- Non-root application container
- Environment-based configuration
- Automated testing with Pytest
- GitHub Actions CI/CD pipeline
- Automated Docker Hub image publishing
- Optimized, production-oriented Docker image

---

## Project Structure

```text
devops-production-app/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── migrations/
│   ├── versions/
│   ├── alembic.ini
│   ├── env.py
│   └── script.py.mako
├── nginx/
│   └── nginx.conf
├── tests/
│   ├── conftest.py
│   └── test_app.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── README.md
├── models.py
└── requirements.txt
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd devops-production-app
```

### 2. Configure environment variables

Create your local environment file from the example:

```bash
cp .env.example .env
```

Update `.env` with your local configuration.

> **Note:** Never commit `.env` to Git. Secrets and passwords must stay out of the repository.

### 3. Start the application

The production-style Compose configuration pulls the published Docker Hub image:

```bash
docker compose pull
docker compose up -d
```

### 4. Verify running containers

```bash
docker compose ps
```

Expected services: `db`, `web`, `nginx`

### 5. Check application health

```bash
curl http://localhost/health
```

Expected response:

```json
{"status": "healthy"}
```

### 6. Open the application

```text
http://localhost
```

---

## Docker Hub Image

The application image is published to Docker Hub:

```text
azeemamir/devops-production-app:latest
```

Pull it manually with:

```bash
docker pull azeemamir/devops-production-app:latest
```

The Compose configuration uses this published image for the Flask web service.

---

## Testing

Run the test suite inside the running web container:

```bash
docker compose exec web pytest -v
```

The GitHub Actions pipeline also runs the full automated test suite before publishing a new Docker image.

---

## Health Check

```text
GET /health
```

```bash
curl http://localhost/health
```

Expected response:

```json
{"status": "healthy"}
```

This endpoint provides a simple, standard way to verify that the application is running correctly — useful for uptime checks, load balancers, and orchestration health probes.

---

## Database

The application uses **PostgreSQL 16**, with data persisted in a named Docker volume: `postgres_data`.

Stop the application without deleting the database volume:

```bash
docker compose down
```

Stop the application **and** remove the database volume:

```bash
docker compose down -v
```

> **Warning:** Removing the volume permanently deletes the PostgreSQL data stored in it.

---

## Nginx

Nginx sits in front of the Flask application as a reverse proxy:

```text
Client → Nginx :80 → Flask :5000 → PostgreSQL :5432
```

Flask is kept behind Nginx rather than being exposed directly as the public endpoint, which allows for centralized routing, buffering, and (in a real production deployment) TLS termination and load balancing.

---

## Security

- The Flask container runs as a **non-root user**.
- Sensitive configuration is provided through environment variables, not hardcoded values.
- `.env` is excluded from Git via `.gitignore`.
- `.dockerignore` keeps unnecessary files out of the Docker build context.
- No secrets, passwords, API keys, or access tokens are stored in the repository.
- The application image has been optimized to minimize unnecessary contents and reduce attack surface.

---

## Useful Docker Commands

| Command | Description |
|---|---|
| `docker compose ps` | View running containers |
| `docker compose logs -f` | View all container logs |
| `docker compose logs -f web` | View Flask logs |
| `docker compose logs -f nginx` | View Nginx logs |
| `docker compose logs -f db` | View PostgreSQL logs |
| `docker compose pull` | Pull the latest image |
| `docker compose up -d` | Start / restart the application |
| `docker compose down` | Stop the application |

---

## DevOps Concepts Demonstrated

This project demonstrates hands-on, practical experience with:

- Linux, Git, and GitHub
- Docker and Docker Compose
- Container networking and volumes
- PostgreSQL and database migrations
- Flask application development
- Nginx reverse proxying
- Health checks and logging
- Container security and non-root containers
- Automated testing
- GitHub Actions CI/CD
- Docker Hub image publishing
- Docker image optimization

---

## Project Goal

The goal of this project is to demonstrate how a traditional Python web application can be transformed into a containerized, tested, secured, and deployment-ready application using practical, industry-standard DevOps tools and workflows — from local development through to automated CI/CD delivery.

---

## Author

**Azeem Amir**
DevOps Engineer / Cloud & Automation Enthusiast
GitHub: [`azeemamir-maga`](https://github.com/azeemamir-maga)

---

## License

This project is licensed under the [MIT License](LICENSE).
