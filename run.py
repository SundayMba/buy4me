# run.py

from api import create_app
from api.v1.models import db
from flask_migrate import Migrate

app = create_app('development')
migrate = Migrate(app, db)

if __name__ == "__main__":
	app.run()
