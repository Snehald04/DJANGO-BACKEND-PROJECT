# Django Backend Project - Docker Setup & Deployment

## 1. Project Setup
- Django backend project is pushed to GitHub.
- Includes:
  - Dockerfile
  - requirements.txt
  - Django app code


## 2. Clone Repository
Clone the repository to local system:
git clone https://github.com/<your-username>/DJANGO-BACKEND-PROJECT.git

cd DJANGO-BACKEND-PROJECT


## 3. Build Docker Image
Build the Docker image using:
docker build -t django-app .


## 4. Run Docker Container
Run the container with port mapping:
docker run -p 8000:8000 -it django-app


## 5. Apply Migrations
Run migrations inside Docker:
docker exec -it <container_id> python manage.py migrate


## 6. Access Application
- Admin Panel:
  http://127.0.0.1:8000/admin/


## 7. API Testing
Test APIs using Postman:

### Signup API
POST http://127.0.0.1:8000/api/signup/

Sample Request Body:
{
  "username": "testuser",
  "password": "Test@123",
  "email": "test@example.com",
  "full_name": "Test User",
  "address": "Pune",
  "mobile_number": "1234567890"
}


## 8. Issues Faced & Fixes
- API was failing due to incorrect JSON parsing.
- Fixed by replacing:
  json.loads(request.body)
  with:
  request.data


## 9. Current Status
- Docker build successful
- Container running successfully
- Admin panel working
- APIs (Signup/Login) working
