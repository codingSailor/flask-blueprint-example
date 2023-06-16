from flask import Blueprint

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route('/')
def index():
    return "This is an product api call"