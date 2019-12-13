from flask import jsonify
from web import app
from web.utils.decorators import authenticated_only
from web.models.users import User


@app.route('/')
@authenticated_only
def index():
    users = User.query.all()
    return jsonify(users)
