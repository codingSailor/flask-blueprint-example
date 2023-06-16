from flask import Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    return "This is an core api call"