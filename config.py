import os

DB_ENGINE=os.getenv("DB_ENGINE")
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")


URI = f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Config:
    SWAGGER = {
        "title": "BUY4ME E-Commerce Restful API",
        "uiversion": 3
    }
    SQLALCHEMY_DATABASE_URI = URI

class Development(Config):
    DEBUG = True

config = {
    "dev": Development
}