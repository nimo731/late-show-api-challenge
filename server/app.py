from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config')
    db.init_app(app)
    migrate.init_app(app, db)
 

    @app.route('/')
    def index():
        return "API is running!"

    return app
