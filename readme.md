# Task Manager - Flask & PostgreSQL

A full-stack Task Manager application built with Flask, PostgreSQL (Docker), and SQLAlchemy. This application allows users to create, read, update, delete, and filter tasks with an intuitive web interface.

---

##  Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)

---

## Features

- Create new tasks with title, description, status, and due date
- View all tasks with filtering options (by status, search query, sort order)
- Update existing tasks
- Delete tasks
- Filter tasks by status (todo, in-progress, completed)
- Search tasks by title
- Sort tasks by creation date (ascending/descending)
- Responsive web interface

---

## Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy
- **Database**: PostgreSQL (running in Docker)
- **Frontend**: HTML, Jinja2 Templates
- **Environment Management**: python-dotenv

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Docker** - [Install Docker](https://docs.docker.com/get-docker/)
- **Git** (optional, for cloning) - [Install Git](https://git-scm.com/downloads/)

---

## Project Structure

```
Task_Manager/
├── venv/                       # Virtual environment (created during setup)
├── config/
│   └── db.py                   # Database configuration
├── controllers/
│   └── controllers.py          # API route handlers
├── models/
│   └── db_model.py             # SQLAlchemy models
├── templates/
│   ├── index.html              # Home page
│   ├── add_task.html           # Add task page
│   ├── all_tasks.html          # All tasks display
│   └── task.html               # Single task display
├── app.py                      # Main Flask application
├── init_db.py                  # Database initialization script
├── .env                        # Environment variables (create this)
└── README.md                   # This file
```

---

## Installation & Setup

Follow these steps carefully to set up the project on your local machine.

### Step 1: Clone or Download the Project

```bash
# If using Git
git clone <your-repository-url>
cd Task_Manager

# Or download and extract the project folder, then navigate to it
cd path/to/Task_Manager
```

### Step 2: Create Virtual Environment

**IMPORTANT**: If you encounter issues with the virtual environment, delete the `venv` folder and recreate it.

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

### Step 3: Install Dependencies

```bash
# Install Flask and required packages
pip install flask
pip install flask-sqlalchemy
pip install psycopg2-binary
pip install python-dotenv
```

**Alternative**: If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Create Environment File

Create a `.env` file in the project root directory with the following content:

```env
# PostgreSQL Database Configuration
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/pythondb

# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
```

**Environment Variables Explanation**:
- `DATABASE_URL`: PostgreSQL connection string
  - Format: `postgresql://username:password@host:port/database_name`
  - `postgres:postgres` - Default PostgreSQL username and password
  - `localhost:5432` - PostgreSQL host and port
  - `pythondb` - Database name

---

## 🗄 Database Setup

### Step 1: Start PostgreSQL Container

```bash
# Start the PostgreSQL container (if already created)
docker start postgres-db

# If the container doesn't exist, create it first:
docker run --name postgres-db \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=pythondb \
  -p 5432:5432 \
  -d postgres:latest
```

### Step 2: Verify Container is Running

```bash
# Check if container is running
docker ps

# You should see postgres-db in the list
```

### Step 3: Initialize Database

Run the database initialization script to create tables:

```bash
# Make sure your virtual environment is activated
python3 init_db.py
```

### Step 4: Verify Database Setup

```bash
# Access PostgreSQL database
docker exec -it postgres-db psql -U postgres -d pythondb

# Inside psql, check the table
pythondb=# \dt                    # List all tables
pythondb=# SELECT * FROM alltask; # View all tasks (should be empty initially)
pythondb=# \q                     # Quit psql
```

**Common PostgreSQL Commands**:
```sql
\dt              -- List all tables
\d alltask       -- Describe alltask table structure
SELECT * FROM alltask;           -- View all tasks
SELECT * FROM alltask WHERE id=1; -- View specific task
\q               -- Quit psql
```

---

## Running the Application

### Step 1: Ensure Virtual Environment is Active

```bash
# Activate if not already active
source venv/bin/activate
```

### Step 2: Ensure PostgreSQL is Running

```bash
# Check container status
docker ps

# If not running, start it
docker start postgres-db
```

### Step 3: Run Flask Application

```bash
# Run the server
flask run

# Or alternatively
python3 app.py
```

### Step 4: Access the Application

Open your web browser and navigate to:

- **Home Page**: http://127.0.0.1:5000
- **All Tasks**: http://127.0.0.1:5000/api/tasks
- **Add Task Page**: http://127.0.0.1:5000/add-task
- **Specific Task**: http://127.0.0.1:5000/api/tasks/<id>

---

##  API Endpoints

### 1. Get All Tasks (with Filtering)

```http
GET /api/tasks
```

**Query Parameters**:
- `status` - Filter by status (todo, in-progress, completed)
- `q` - Search by title (case-insensitive)
- `sort` - Sort by creation date (asc, desc)

**Examples**:
```
GET /api/tasks                           # Get all tasks
GET /api/tasks?status=todo               # Get only todo tasks
GET /api/tasks?q=meeting                 # Search tasks with "meeting" in title
GET /api/tasks?sort=desc                 # Get tasks sorted newest first
GET /api/tasks?status=todo&sort=asc      # Combine filters
```

### 2. Create New Task

```http
POST /api/tasks
Content-Type: application/x-www-form-urlencoded

title=Task Title
description=Task Description
status=todo
due_date=2024-12-31
```

### 3. Get Specific Task

```http
GET /api/tasks/<id>
```

**Example**: `GET /api/tasks/1`

### 4. Update Task

```http
PUT /api/tasks/<id>
Content-Type: application/json

{
  "title": "Updated Title",
  "description": "Updated Description",
  "status": "in-progress",
  "due_date": "2024-12-31"
}
```

### 5. Delete Task

```http
DELETE /api/tasks/<id>
```

**Example**: `DELETE /api/tasks/1`



**Example cURL Commands**:

```bash
# Get all tasks
curl http://127.0.0.1:5000/api/tasks

# Create a task
curl -X POST http://127.0.0.1:5000/api/tasks \
  -d "title=New Task" \
  -d "description=Task description" \
  -d "status=todo" \
  -d "due_date=2024-12-31"

# Update a task
curl -X PUT http://127.0.0.1:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Task","status":"completed"}'

# Delete a task
curl -X DELETE http://127.0.0.1:5000/api/tasks/1
```

---

## 🔧 Troubleshooting

### Issue 1: "flask: command not found"

**Solution**: Recreate the virtual environment

```bash
deactivate                # Exit current venv
rm -rf venv              # Delete old venv
python3 -m venv venv     # Create new venv
source venv/bin/activate # Activate
pip install flask flask-sqlalchemy psycopg2-binary python-dotenv
```

### Issue 2: "Connection refused" to PostgreSQL

**Solutions**:

1. Check if Docker is running:
```bash
docker ps
```

2. Start PostgreSQL container:
```bash
docker start postgres-db
```

3. Verify connection details in `.env` file match the container configuration

### Issue 3: "relation 'alltask' does not exist"

**Solution**: Run the database initialization script

```bash
python3 init_db.py
```

### Issue 4: Port 5000 already in use

**Solution**: Either:

1. Kill the process using port 5000:
```bash
# Find process
lsof -i :5000

# Kill it
kill -9 <PID>
```

2. Or run Flask on a different port:
```bash
flask run --port 5001
```

### Issue 5: Docker container not starting

**Solution**: Check Docker logs

```bash
docker logs postgres-db
```

If the container doesn't exist, create it:
```bash
docker run --name postgres-db \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=pythondb \
  -p 5432:5432 \
  -d postgres:latest
```

---

## Database Schema

**Table**: `alltask`

| Column | Type | Description |
|--------|------|-------------|
| id | Serial (Primary Key) | Auto-incrementing task ID |
| title | String(200) | Task title (required) |
| description | Text | Task description (optional) |
| status | String(20) | Task status (default: 'todo') |
| due_date | Date | Task due date (optional) |
| created_at | DateTime | Creation timestamp (auto) |

**Status Values**: `todo`, `in-progress`, `completed`

---

## For Instructors

This project demonstrates:

1. **RESTful API Design** - Proper HTTP methods (GET, POST, PUT, DELETE)
2. **Database Integration** - PostgreSQL with SQLAlchemy ORM
3. **Containerization** - Docker for database management
4. **Environment Management** - Using .env for configuration
5. **MVC Pattern** - Separated models, controllers, and views
6. **Query Filtering** - Search, filter, and sort functionality
7. **Error Handling** - Proper HTTP status codes

**Quick Start for Instructors**:

```bash
# 1. Start PostgreSQL
docker start postgres-db

# 2. Activate environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy psycopg2-binary python-dotenv

# 3. Create .env file with DATABASE_URL (see Step 4 above)

# 4. Initialize database
python3 init_db.py

# 5. Run application
flask run

# 6. Access at http://127.0.0.1:5000
```


