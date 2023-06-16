from flask import Blueprint

models = Blueprint('models', __name__)

@models.route('/')
def index():
    return "This is an models api call"