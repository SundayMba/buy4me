from api import create_app
import os
from dotenv import load_dotenv

"""Load all Environment variables"""
load_dotenv()

FLASK_ENV = os.getenv("FLASK_ENV") 
"""Application Entry Point"""
app = create_app(FLASK_ENV)