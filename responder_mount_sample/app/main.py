from flask import Flask
from responder import API

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"hello, {name}"


api = API()
api.mount("/", app)
