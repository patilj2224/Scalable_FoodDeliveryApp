from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User created", "userId": user_id}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    # CRITICAL: listen on all interfaces
    app.run(host="0.0.0.0", port=5000)
