from typing import List
from .service import Service
import os
from flask import jsonify

class FileService(Service):
    FILE_LOCATION: str = "./api/images/"
    categories = {"product", "collection", "popular"}
    allowed_extension: List[str] = {"jpg", "jpeg", "gif", "png"}

    def __init__(self):
        """initialize the file service"""
        # self.setup_file_location(self.FILE_LOCATION)

    def verify_file_extension(self, filename: str):
        """check if file contains a valid file extension"""
        return '.' in filename and filename.rsplit(".", 1)[1] in self.allowed_extension

    def save(self, file, filename: str, category: str):
        if category.lower() not in self.categories:
            return 400
        
        file_location = self.FILE_LOCATION + category
        self.setup_file_location(file_location)
        file.save(os.path.join(file_location, filename))
        return 200
    
    def create(self):
        pass

    def setup_file_location(self, location):
        if not os.path.exists(location):
            os.makedirs(location)

    def fetch_all(self):
        pass

    def fetch_by_id(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
fileService = FileService()