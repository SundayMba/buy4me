import os

# Fetch environment variables
DB_ENGINE=os.getenv("DB_ENGINE")
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT", 3306) # Default MySQL port
DB_NAME=os.getenv("DB_NAME")

# Create the database URI
URI = f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Config:
	# Swagger configuration
	SWAGGER = {
		"title": "BUY4ME E-Commerce Restful API",
		"uiversion": 3
	}
	# SQLAlchemy database configuration
	SQLALCHEMY_DATABASE_URI = URI
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
	# Enable debugging in development
	DEBUG = True

# Define configuration options
config = {
	"dev": Development
}