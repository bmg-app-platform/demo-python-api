from flask import Flask, jsonify, request
import urllib.request
import os

app = Flask(__name__)

live = [
    { 
        'application': os.getenv('APP_NAME'), 
        'status': 'Im alive' 
    }
]

ready = [
    { 
        'application': os.getenv('APP_NAME'), 
        'status': 'Im ready' 
    }
]

not_ready = [
    { 
        'application': os.getenv('APP_NAME'), 
        'status': 'Stoppppp Im busy!!' 
    }
]

jobs = []

versions = [
    { 
        'application': os.getenv('APP_NAME'), 
        'version': 'v10.0.0' 
    }
]

runtime_details = [
    { 
        'application': os.getenv('APP_NAME'), 
        'hostname': os.getenv('HOSTNAME')
    }
]

print("API running on port : {} ".format(os.getenv('FLASK_RUN_PORT')))

@app.route("/livez")
def liveness_probe():
    return jsonify(live)

@app.route("/readyz")
def radiness_probe():
    if urllib.request.urlopen("https://www.google.com").getcode() == 200:
        return jsonify(ready)
    else:
        return jsonify(not_ready)

@app.route("/getjobs")
def get_jobs():
    return jsonify(jobs)

@app.route('/createjobs', methods=['POST'])
def add_jobs():
    jobs.append(request.get_json())
    return '', 204

@app.route("/version")
def get_version():
    return jsonify(versions)

@app.route("/runtimez")
def get_runtime_details():
    return jsonify(runtime_details)
