from flask import Flask, jsonify
from flask_login import LoginManager
from config import Config
from .models import db, bcrypt
from .routes import auth_bp, api_bp
from .utils.mail import mail

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)


def create_app():
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.config['DEBUG'] = True
    return app
