# from flask import Blueprint
from flask import Flask

# app = Blueprint("team", __name__)
app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_all():
    return "all the teams"


@app.route("/<int:id>")
def get_one(id):
    return f"team{id}"
