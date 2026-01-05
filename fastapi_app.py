from fastapi import FastAPI

app = FastAPI()

# SERVICE LAYER

users = []

def get_all_users_service():
    return users

def create_user_service(user_data: dict):
    users.append(user_data)
    return {
        "message": "User created successfully",
        "user": user_data
    }

# CONTROLLER LAYER

def get_users_controller():
    return get_all_users_service()

def create_user_controller(user: dict):
    return create_user_service(user)

# routes
@app.get("/users")
def get_users_route():
    return get_users_controller()

@app.post("/users")
def create_user_route(user: dict):
    return create_user_controller(user)
