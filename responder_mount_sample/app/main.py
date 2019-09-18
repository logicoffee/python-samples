from flask import Flask
from responder import API

from controllers import team

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"hello, {name}"


api = API()
api.mount("/hello", app)
api.mount("/teams", team.app)


@api.route("/healthcheck")
def healthcheck(req, resp):
    resp.text = "I am healthy."
