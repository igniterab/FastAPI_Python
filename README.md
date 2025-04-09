# 📝 FastAPI Task Manager

A simple Task Management API built with **FastAPI**, **SQLModel**, **PostgreSQL**, and **JWT Authentication**.

---

## 🚀 Features

- User registration and login with JWT tokens
- Create, view, update, delete (soft) personal tasks
- Filter tasks by title (fuzzy) and date
- PostgreSQL database using SQLModel (SQLAlchemy ORM)
- Input validation with Pydantic
- Dependency-injected database sessions
- Dockerized setup with `docker-compose`

---

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- SQLModel / SQLAlchemy
- PostgreSQL
- PyJWT / JOSE
- Docker & Docker Compose
- Passlib (password hashing)

---

## 📁 Project Structure

```
app/
├── api/            # Route handlers
├── core/           # Settings, security
├── crud/           # Database operations
├── db/             # Models and DB session
├── dependencies/   # Auth dependencies
├── schemas/        # Pydantic schemas
main.py             # FastAPI app
Dockerfile
```

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Docker & Docker Compose installed

---

### 🔧 Environment Variables

Create a `.env` file at the root:

```
SECRET_KEY=supersecretkey123
ALGORITHM=HS256
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

### 🐳 Run with Docker

```bash
docker-compose up --build
```

- App: [http://localhost:8008](http://localhost:8000)
- Docs: [http://localhost:8008/docs](http://localhost:8000/docs)

---

### 🎯 API Usage

#### 🔐 Auth

- `POST /auth/register/` – Register a user
- `POST /auth/login/` – Login and receive access token

#### ✅ Tasks (authenticated)


- `POST /tasks/` – Create a task
- `GET /tasks/` – List all your tasks with optional filters:
  - `?query=meeting&date=2025-04-08`
- `GET /tasks/{task_id}` – Get one task
- `PUT /tasks/{task_id}` – Update a task
- `DELETE /tasks/{task_id}` – Soft delete

---

## 📬 Example Payloads

### Register

```json
{
  "username": "ashish",
  "email": "ashish@gmail.com",
  "password": "secure123"
}
```

### Login

```json
{
  "username": "ashish",
  "email": "ashish@gmail.com",
  "password": "secure123"
}
```

### Create Task

```json
{
  "title": "Prepare report",
  "description": "Due tomorrow"
}
```

---

## 🛠️ Dev Commands

```bash
# Rebuild containers
docker-compose up --build

# Stop containers
docker-compose down
```

---
