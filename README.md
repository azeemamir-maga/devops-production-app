# DevOps Production App

A Production-Style Flask Web Application Built With Docker, PostgreSQL, And Nginx.

This Project Demonstrates How A Python Web Application Can Be Containerized, Connected To A PostgreSQL Database, Served Through An Nginx Reverse Proxy, Tested, And Prepared For CI/CD With GitHub Actions.

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
```

## Tech Stack

* Python
* Flask
* SQLAlchemy
* PostgreSQL 16
* Docker
* Docker Compose
* Nginx
* GitHub Actions
* Docker Hub
* Linux / Ubuntu

## Features

* Flask Application Factory
* PostgreSQL Database
* CRUD API
* Database Migrations
* Dockerized Flask Application
* Docker Compose Multi-Container Architecture
* Nginx Reverse Proxy
* Application Health Check
* Persistent PostgreSQL Storage
* Non-Root Application Container
* Automated Testing
* CI/CD Pipeline
* Docker Image Optimization

## Project Structure

```text
devops-production-app/
├── app/
├── migrations/
├── nginx/
├── tests/
├── docker/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Run Locally

### 1. Clone The Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd devops-production-app
```

### 2. Start The Application

```bash
docker compose up --build -d
```

### 3. Check Running Containers

```bash
docker compose ps
```

### 4. Check Application Health

```bash
curl http://localhost/health
```

Expected Response:

```json
{"status":"healthy"}
```

### 5. Open The Application

Open:

```text
http://localhost
```

## Useful Docker Commands

View Running Containers:

```bash
docker compose ps
```

View Logs:

```bash
docker compose logs -f
```

View Web Application Logs:

```bash
docker compose logs -f web
```

View Nginx Logs:

```bash
docker compose logs -f nginx
```

Stop The Application:

```bash
docker compose down
```

Stop The Application And Remove Database Volume:

```bash
docker compose down -v
```

## Testing

Run The Test Suite Inside The Web Container:

```bash
docker compose exec web pytest
```

## Health Check

The Application Provides A Health Endpoint:

```text
GET /health
```

Example:

```bash
curl http://localhost/health
```

Response:

```json
{"status":"healthy"}
```

This Endpoint Can Be Used To Verify That The Application Is Running Correctly.

## Database

The Application Uses PostgreSQL 16 For Persistent Data Storage.

Docker Compose Provides A Named Volume:

```text
postgres_data
```

This Allows PostgreSQL Data To Persist Across Container Restarts.

## Nginx

Nginx Acts As A Reverse Proxy In Front Of The Flask Application.

The Request Flow Is:

```text
Client
  ↓
Nginx :80
  ↓
Flask :5000
  ↓
PostgreSQL :5432
```

The Flask Application Is Not Directly Exposed To The Host. Nginx Provides The Public HTTP Entry Point.

## Security

The Application Container Runs Using A Non-Root User.

Environment Variables Are Used For Configuration And Sensitive Values.

The `.env` File Is Excluded From Git Using `.gitignore`.

Never Commit Passwords, API Keys, Tokens, Or Other Secrets To The Repository.

## DevOps Concepts Demonstrated

This Project Demonstrates Practical Experience With:

* Linux
* Git And GitHub
* Docker
* Docker Compose
* Container Networking
* Docker Volumes
* PostgreSQL
* Flask
* Nginx
* Health Checks
* Container Security
* Automated Testing
* CI/CD
* Docker Image Optimization

## CI/CD

GitHub Actions Is Used To Automate The Software Delivery Workflow.

The CI/CD Pipeline Can:

1. Check Out The Repository
2. Install Dependencies
3. Run Tests
4. Build The Docker Image
5. Authenticate With Docker Hub
6. Push The Docker Image

## Project Goal

The Goal Of This Project Is To Demonstrate How A Traditional Web Application Can Be Transformed Into A Containerized, Tested, And Deployment-Ready DevOps Project.

## Author

**Azeem Amir**

DevOps Engineer / Cloud & Automation Enthusiast

GitHub: `azeemamir-maga`
