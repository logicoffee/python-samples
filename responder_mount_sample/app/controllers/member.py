# from flask import Blueprint
from flask import Flask

# app = Blueprint("member", __name__)
app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_all(team_id):
    return f"all the members of team{team_id}"


@app.route("/<int:id>")
def get_one(team_id, id):
    return f"member{id} of team{team_id}"
