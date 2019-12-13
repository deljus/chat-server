from flask import jsonify, Blueprint
from ..utils.decorators import authenticated_only
from ..models.users import User

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users')
def index():
    users = User.query.all()
    return jsonify(success=True)
