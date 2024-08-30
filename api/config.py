
class Config:
    SWAGGER = {
        "title": "BUY4ME E-Commerce Restful API",
        "uiversion": 3
    }


class Development(Config):
    DEBUG = True

config = {
    "dev": Development
}