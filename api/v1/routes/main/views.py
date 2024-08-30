from . import main
from flask import jsonify

@main.route("/<name>", methods=["GET"])
def main(name):
    """
    A simple greeting API.
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name to greet.
    responses:
      200:
        description: A greeting message.
        examples:
          application/json: { "message": "Hello, John!" }
    """
    return jsonify(message=f"Hello {name}, Welcome to the home page")
