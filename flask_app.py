from flask import Flask, request, jsonify

app = Flask(__name__)


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


# CONTROLLER LAYER

def get_users_controller():
    users = get_all_users_service()
    return jsonify(users), 200

def create_user_controller():
    data = request.json
    response = create_user_service(data)
    return jsonify(response), 201

# ROUTES

@app.route("/users", methods=["GET"])
def get_users_route():
    return get_users_controller()

@app.route("/users", methods=["POST"])
def create_user_route():
    return create_user_controller()


# SERVER

if __name__ == "__main__":
    app.run(debug=True)
