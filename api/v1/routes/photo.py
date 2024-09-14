from flask import request, jsonify, url_for, send_from_directory, send_file
from . import photo_bp
from werkzeug.utils import secure_filename
from ..services.file_service import fileService
from datetime import datetime, timezone
from uuid6 import uuid7
import os

@photo_bp.route("/upload-image/<category>", methods=["POST"])
def upload_image(category):
    """Upload a product image
    
    Keyword arguments:
    argument -- None
    Return: return_description
    """
    #check if an image is uploaded with the key 'image'
    if 'image' not in request.files:
        return jsonify({
            "error": "image file not included in the request"
        }), 400
    
    # extract the image file
    file = request.files["image"]

    # check if the extracted file contains the actual image
    if file.filename == '':
        return jsonify({
            "error": "no file part selected"
        }), 400
    
    # check for valid file extensions
    if not fileService.verify_file_extension(file.filename):
        return jsonify({
            "error": "not a valid file extension"
        }), 400
    
    # secure the original filename from malicious attacks
    filename = secure_filename(file.filename)

    # Generate a unique filename using uuid
    unique_filename = f'{uuid7().hex}_{filename}'

    # save the file
    if fileService.save(file, unique_filename, category) == 400:
        return jsonify({
            'error': "invalid file category"
        }), 400
    
    # generate url for the image
    image_url = url_for("photo.uploaded_file", category=category, filename=unique_filename, _external=True)

    return jsonify({
        "message": "uploaded successfully",
        "image_url": image_url
    }), 201

@photo_bp.route("/uploads/<category>/<filename>", methods=["GET"])
def uploaded_file(filename, category):
    return send_from_directory(f"./images/{category}", filename)


@photo_bp.route("/remove-image/<category>/<image_name>", methods=["DELETE"])
def remove_image(category, image_name):
    file_path = os.path.join("./api/images", category, image_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({
            "message": "file deleted successfully"
        })
    else:
        return jsonify({
            "error": "file does not exists"
        }), 400