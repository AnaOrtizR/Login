from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config["JWT_SECRET_KEY"] = "GkY%^63w#%h@HT6" 
    jwt = JWTManager(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app