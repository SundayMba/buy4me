import os

# Fetch environment variables for database configuration
DB_ENGINE = os.getenv("DB_ENGINE", "mysql")
DB_USERNAME = os.getenv("DB_USERNAME", "Matthew")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 3306)
DB_NAME = os.getenv("DB_NAME", "buy4me")

# Construct the database URI
# Directly set the database URI
URI = "mysql://Matthew:root@localhost:3306/buy4me"

# Debug the URI (optional)
print(f"Database URI: {URI}")

class Config:
	# SQLAlchemy database configuration
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://Matthew:root@localhost:3306/buy4me')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Swagger configuration
	SWAGGER = {
		"title": "BUY4ME E-Commerce Restful API",
		"uiversion": 3
	}

class Development(Config):
	DEBUG = True

# Define configuration options
config = {
	"dev": Development
}