from flasgger import Swagger
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

swagger = Swagger()
migrate = Migrate()
db = SQLAlchemy()
cors = CORS()
jwt = JWTManager()
