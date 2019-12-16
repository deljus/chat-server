from flask import Flask, render_template
from flask_login import LoginManager
from flask_cors import CORS
from config import Config
from .models import db, bcrypt
from .routes import auth_bp, api_bp
from .utils.mail import mail
import os


app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)
if os.environ.get('FLASK_ENV'):
    CORS(app)


@app.route('/')
def index():
    return render_template('/index.html')


def create_app():
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    app.config['DEBUG'] = True
    return app
