from flask import Blueprint

general = Blueprint('general', __name__)

@general.route('/')
def index():
    return "This is an general api call"