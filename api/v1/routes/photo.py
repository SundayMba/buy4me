from flask import request, jsonify, url_for, send_from_directory, send_file
from . import photo_bp
from werkzeug.utils import secure_filename
from ..services.file_service import fileService
from datetime import datetime, timezone
from uuid6 import uuid7
import os
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url


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
    

    # Generate a unique filename using uuid
    unique_filename = f'{category}_{uuid7().hex}'

    # Upload an image
    upload_result = cloudinary.uploader.upload(file, public_id=unique_filename)

    # Optimize delivery by resizing and applying auto-format and auto-quality
    optimize_url, _ = cloudinary_url(unique_filename, fetch_format="auto", quality="auto")
    print(optimize_url)

    return jsonify({
        "message": "uploaded successfully",
        "image_url": optimize_url,
        "status": 201
    }), 201

@photo_bp.route("/product-image/<category>/<filename>", methods=["GET"])
def uploaded_file(filename, category):
    return send_from_directory(f"./images/{category}", filename)


@photo_bp.route("/delete-image", methods=["DELETE"])
def delete_image():
    # deserialize the json object to python dict
    payload = request.json
    image_url = payload.get("image_url")
    public_id = image_url.split('/')[-1]
    print(public_id)
    result = cloudinary.uploader.destroy(public_id=public_id)
    if result["result"] == 'ok':
        return jsonify({"message": "image deleted successfully"}), 200
    else:
        return jsonify({
            "message": "no image found"
        }), 404
