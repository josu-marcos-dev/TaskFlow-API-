# 🚀 TaskFlow API

A production-inspired REST API for task and project management, built to simulate real-world backend engineering challenges.

---

## 📌 Overview

TaskFlow API is a backend system that allows users to manage projects and tasks with authentication, relational database persistence, and a structured architecture.

This project focuses on **real-world backend fundamentals**, including:

* API design
* Authentication & authorization
* Database modeling
* Clean architecture

> This is not just a CRUD project — it is a structured backend system built from scratch with engineering decisions, trade-offs, and real challenges.

---

## 🧠 What This Project Demonstrates

* Ability to design and build REST APIs
* Understanding of backend architecture and separation of concerns
* Experience with relational databases and ORM
* Implementation of authentication using JWT
* Real problem-solving without over-reliance on AI tools

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **Docker**
* **JWT Authentication**
* **Linux / CLI**
* **Git & GitHub**

---

## 🏗️ Architecture

The project follows a layered architecture:

```
app/
├── routes/       # API endpoints
├── services/     # Business logic
├── models/       # Database models
├── schemas/      # Data validation (Pydantic)
├── database/     # DB connection & session
```

### Key Principles

* Separation of concerns
* Scalable structure
* Clean and maintainable code organization

---

## 🔐 Authentication

Authentication is implemented using JWT:

* Token generation on login
* Protected routes using dependency injection
* Validation of user identity before accessing resources

---

## 🧩 Features

* User management
* Project management
* Task management
* Authentication & authorization
* Full CRUD operations
* Relational database integration

---

## 🗄️ Database Design

Relational structure:

```
User → Project → Task
```

* One user can have multiple projects
* One project can have multiple tasks
* Relationships handled via SQLAlchemy ORM

---

## ⚙️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/josu-marcos-dev/TaskFlow-API-
cd TaskFlow-API-
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

### 5. Access API docs

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker (Optional)

The project can be containerized to ensure environment consistency.

* Eliminates dependency issues
* Enables reproducibility across systems

---

## 🚧 Challenges Faced

This project was built with minimal reliance on AI tools, which led to several important challenges:

* Understanding new technologies from scratch (Docker, PostgreSQL, FastAPI)
* Debugging communication issues between models, schemas, and routes
* Designing proper relationships between entities
* Implementing authentication and access control
* Structuring the project using best practices

---

## 📈 Key Learnings

* REST API design and best practices
* Backend architecture organization
* Database modeling and relationships
* Debugging complex integration issues
* Importance of naming consistency across layers
* Real-world development workflow

---

## 💡 Future Improvements

* Add automated tests
* Implement role-based authorization
* Add pagination and filtering
* Improve error handling and logging
* Deploy to cloud environment (AWS, Railway, etc.)

---

## 📊 Why This Project Matters

This project represents a transition from:

> "learning concepts" → "building real backend systems"

It demonstrates the ability to:

* Build systems from scratch
* Make engineering decisions
* Handle real-world complexity

---

## 👨‍💻 Author

Developed by **Josué Marcos**

---

## ⭐ Final Note

This is a foundational backend project designed to simulate real-world engineering scenarios and strengthen core backend skills.

If you're a recruiter or developer reviewing this project:

👉 This is not just code — it's a learning journey translated into a working system.
