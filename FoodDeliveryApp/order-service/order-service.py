from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

orders = {}

@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get("userId")

    # Call user-service to check if user exists
    try:
        resp = requests.get(f"http://user-service:5000/users/{user_id}")
        if resp.status_code != 200:
            return jsonify({"error": "User not found"}), 400
    except Exception as e:
        return jsonify({"error": "User-service unreachable"}), 500

    # If user exists, save order
    order_id = data.get("orderId")
    orders[order_id] = data
    return jsonify({"message": "Order created", "order": data}), 201

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404
if __name__ == "__main__":
    # CRITICAL: listen on all interfaces and correct port
    app.run(host="0.0.0.0", port=5001)
