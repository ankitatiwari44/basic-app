from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(
    app,
    title="User Management API",
    description="Basic GET and POST APIs using Flask with Swagger documentation",
    version="1.0.0"
)


# SERVICE LAYER

users = []

def get_all_users_service():
    return users

def create_user_service(user_data):
    users.append(user_data)
    return {
        "message": "User created successfully",
        "user": user_data
    }


# REQUEST MODEL

user_model = api.model("User", {
    "name": fields.String(required=True, description="User name"),
    "role": fields.String(required=True, description="User role")
})

# ROUTES + CONTROLLERS

@api.route("/users")
class UserResource(Resource):

    @api.response(200, "Success")
    def get(self):
        """Get all users"""
        return get_all_users_service(), 200

    @api.expect(user_model)
    @api.response(201, "User created successfully")
    def post(self):
        """Create a new user"""
        data = request.get_json()
        response = create_user_service(data)
        return response, 201

# SERVER
if __name__ == "__main__":
    app.run(debug=True)
