from flask import Flask, jsonify, request
import os

app = Flask(__name__)

health = [
    { 'application': os.getenv('APP_NAME'), 'status': 'Im ok' }
]

jobs = []

print("API running on port : {} ".format(os.getenv('FLASK_RUN_PORT')))

@app.route("/healthz")
def health_check():
    return jsonify(health)

@app.route("/getjobs")
def get_jobs():
    return jsonify(jobs)

@app.route('/createjobs', methods=['POST'])
def add_jobs():
    jobs.append(request.get_json())
    return '', 204
