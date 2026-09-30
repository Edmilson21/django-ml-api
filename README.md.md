# django-ml-api

REST API built with Django REST Framework integrating Machine Learning, Computer Vision, and JWT authentication. Fully containerized with Docker and PostgreSQL.

## Features

- JWT Authentication (access + refresh token)
- Custom user model with role-based permissions (Admin, Professor, Student)
- CRUD endpoints with Django ViewSets and Routers
- Machine Learning model integration (Scikit-learn + Joblib)
- Computer Vision endpoint with object detection (YOLOv8 + OpenCV)
- Advanced ORM queries with filters and search
- Test suite with pytest-django (87% coverage)
- Dockerized with Docker Compose + PostgreSQL + Gunicorn

## Tech Stack

- **Backend:** Python, Django 5, Django REST Framework
- **Auth:** JWT (djangorestframework-simplejwt)
- **ML:** Scikit-learn, Joblib, NumPy
- **Computer Vision:** YOLOv8 (Ultralytics), OpenCV
- **Database:** PostgreSQL (production), SQLite (development)
- **Deploy:** Docker, Docker Compose, Gunicorn
- **Testing:** pytest, pytest-django, pytest-cov

## Project Structure

```
django-ml-api/
├── users/               # Auth, custom user model, JWT, permissions
├── lessons/             # CRUD with ViewSets, ORM filtering, search
├── predicciones/        # ML prediction endpoint (Scikit-learn)
├── vision/              # Computer Vision endpoint (YOLOv8)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## API Endpoints

### Authentication
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/users/register/` | Register new user | Public |
| POST | `/api/users/login/` | Login, returns JWT tokens | Public |
| POST | `/api/users/token/refresh/` | Refresh access token | Public |
| GET | `/api/users/profile/` | Get current user profile | Required |

### Lessons
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/api/lessons/` | List all lessons | Required |
| POST | `/api/lessons/` | Create lesson | Professor/Admin |
| GET | `/api/lessons/{id}/` | Get lesson detail | Required |
| PUT | `/api/lessons/{id}/` | Update lesson | Professor/Admin |
| DELETE | `/api/lessons/{id}/` | Delete lesson | Professor/Admin |

**Query params:** `?titulo=vocal` `?rol=profesor` `?busqueda=consonante`

### Machine Learning
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/predicciones/predecir/` | Get ML prediction | Required |

### Computer Vision
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/api/vision/detectar/` | Object detection in image | Required |

## Quick Start

### With Docker (recommended)

```bash
# Clone the repo
git clone https://github.com/Edmilson21/django-ml-api.git
cd django-ml-api

# Create .env file
cp .env.example .env

# Build and run
docker-compose up --build

# Apply migrations (in another terminal)
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

### Without Docker

```bash
# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DB_NAME=django_ml_db
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=db
DB_PORT=5432
```

## Running Tests

```bash
pytest -v
pytest --cov=users --cov=lessons -v  # with coverage report
```

## Role-based Permissions

| Action | Student | Professor | Admin |
|--------|---------|-----------|-------|
| View lessons | OK | OK | OK |
| Create lesson | NO | OK | OK |
| Update lesson | NO | OK | OK |
| Delete lesson | NO | OK | OK |
| View profile | OK | OK | OK |

## Author

**Edmilson Nascimento** — Junior ML Engineer  
[GitHub](https://github.com/Edmilson21) · [LinkedIn](https://www.linkedin.com/in/edmilson-lu%C3%ADs-carlos-nascimento-0245a41b4/)
