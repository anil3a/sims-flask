from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_by_name
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    api = Api(
        app,
        version='0.0.1',
        title='Smart Inventory Management API',
        description='API documentation for Smart Inventory Management System'
    )

    from app.routes import register_blueprints
    register_blueprints(app, api)

    return app
