from flask import Blueprint, request, jsonify
from scr.mathlib import Statistics, EmptyDataError

bp = Blueprint("math", __name__)

@bp.route("/mean", methods=["GET", "POST"])
def calculate_mean():
    if request.method == "GET":
        return {"info": "Send a POST with numbers to calculate mean"}
    data = request.json.get("numbers", [])
    result = Statistics.mean(data)
    return {"mean": result}
