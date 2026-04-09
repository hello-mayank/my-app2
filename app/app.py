from flask import Flask, jsonify
import os


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello DevOps Engg")


@app.route("/health")
def health():
    return jsonify(status="OK")


if __name__ == "__main__":
    env = os.getenv("ENV", "development")
    debug = True if env == "development" else False
    app.run(host="0.0.0.0", port=5000, debug=debug)
