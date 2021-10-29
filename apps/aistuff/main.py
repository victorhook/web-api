from flask import Blueprint

api = Blueprint('aistuff', __name__)

@api.route('/ai')
def index():
    return 'Hello ai'

