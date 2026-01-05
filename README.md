# Routes, Controllers, and Services 

## Objective
To demonstrate understanding of servers, routes, controllers, and services
using Flask and FastAPI in a single-file implementation.

## Architecture 
Routes: Define API endpoints
Controllers: Handle request flow
Services: Perform business logic


## APIs
- GET /users
- POST /users

## Setup
1. Create virtual environment
   python -m venv venv
2. Activate environment
   venv\Scripts\activate
3. Install dependencies
   pip install -r requirements.txt

## Run Flask App
python flask_app.py

## Run FastAPI App
uvicorn fastapi_app:app --reload

## Testing
Used Postman to test GET and POST requests.
Successful responses confirm correct routing and logic execution.

