# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def create_message():
    return "Hello, World!"