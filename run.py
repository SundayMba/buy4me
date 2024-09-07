from api import create_app
import os
from dotenv import load_dotenv

"""Load all Environment variables"""
load_dotenv()

FLASK_ENV = os.getenv("FLASK_ENV", "development")

"""Application Entry Point"""
# Map FLASK_ENV to the configuration key (e.g., 'dev' for Development)
if FLASK_ENV == 'development':
	config_name = 'dev'
else:
	config_name = 'default'  # Add more environments as needed

app = create_app(config_name)

if __name__ == "__main__":
	app.run()