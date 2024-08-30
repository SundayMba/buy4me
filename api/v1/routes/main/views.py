from . import main
from flask import jsonify
from  flasgger.utils import swag_from


@main.route("/<name>", methods=["GET"])
@swag_from("../documentation/main/simple_greeting.yml")
def main(name):
    return jsonify(message=f"Hello {name}, Welcome to the home page")
