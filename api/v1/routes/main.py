from . import main_bp
from flask import jsonify
from  flasgger.utils import swag_from


@main_bp.route("/<name>", methods=["GET"])
@swag_from("./documentation/greeting.yml")
def main(name):
    return jsonify(message=f"Hello {name}, Welcome to the home page")
