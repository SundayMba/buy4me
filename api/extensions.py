from flasgger import Swagger
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

swagger = Swagger()
migrate = Migrate()
db = SQLAlchemy()
cors = CORS()