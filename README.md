# Routes, Controllers, and Services – Single File Demo

## Objective
To demonstrate understanding of servers, routes, controllers, and services
using Flask and FastAPI in a single-file implementation.

## Architecture (Conceptual)
Routes: Define API endpoints
Controllers: Handle request flow
Services: Perform business logic
(All implemented in one file for simplicity)

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
Use Postman to test GET and POST requests.
Successful responses confirm correct routing and logic execution.
