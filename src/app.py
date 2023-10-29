from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Ashok"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Ashok Nallasivam",
        "email": "ashoknallasivam@gmail.com",
    }

    preferred_name = request.args.get("preferred_name")
    if preferred_name:
        user_data["preferred_name"] = preferred_name

    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
