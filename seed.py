from run import app
from api.v1.models import *
from api.extensions import db

with app.app_context():
    user = {
        "password": "admin",
        "username": "admin",
        "email": "admin@gmail.com",
        "role": "admin"
    }

    user = User(**user)
    db.session.add(user)
    db.session.commit()
