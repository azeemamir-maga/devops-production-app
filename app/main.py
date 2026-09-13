import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/api/status")
def status():
    return jsonify(
        service="devops-production-app",
        version="0.1.0",
        environment=os.getenv("APP_ENV", "development")
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
