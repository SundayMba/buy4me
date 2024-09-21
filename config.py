import os
import cloudinary

DB_ENGINE=os.getenv("DB_ENGINE")
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")
JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
CLOUDINARY_API_KEY=os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET=os.getenv("CLOUDINARY_API_SECRET")
CLOUDINARY_NAME=os.getenv("CLOUDINARY_NAME")

# cloudinary Configuration       
cloudinary.config( 
    cloud_name = CLOUDINARY_NAME, 
    api_key = CLOUDINARY_API_KEY, 
    api_secret = CLOUDINARY_API_SECRET,
    secure=True
)


URI = f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Config:
    SWAGGER = {
        "title": "BUY4ME E-Commerce Restful API",
        "uiversion": 3
    }
    SQLALCHEMY_DATABASE_URI = URI
    JWT_SECRET_KEY: str = JWT_SECRET_KEY
    SECRET_KEY: str = SECRET_KEY

class Development(Config):
    DEBUG = True

config = {
    "dev": Development
}
