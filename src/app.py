# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_cicd():
    return "Hello, CI/CD with Flask!"
