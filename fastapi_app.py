from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="User Management API",
    description="GET and POST APIs with error handling using FastAPI",
    version="1.0.0"
)


# SERVICE LAYER
users = []

def get_all_users_service():
    try:
        return users
    except Exception as e:
        raise Exception(f"Error fetching users: {str(e)}")

def create_user_service(user_data: dict):
    try:
        users.append(user_data)
        return {
            "message": "User created successfully",
            "user": user_data
        }
    except Exception as e:
        raise Exception(f"Error creating user: {str(e)}")


# CONTROLLER LAYER
def get_users_controller():
    try:
        return get_all_users_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_user_controller(user: dict):
    try:
        if not user.get("name") or not user.get("role"):
            raise HTTPException(
                status_code=400,
                detail="Both 'name' and 'role' are required"
            )
        return create_user_service(user)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# REQUEST MODEL
class User(BaseModel):
    name: str
    role: str


# ROUTES
@app.get("/users")
def get_users_route():
    return get_users_controller()

@app.post("/users")
def create_user_route(user: User):
    return create_user_controller(user.dict())


