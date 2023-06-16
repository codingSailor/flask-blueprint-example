from flask import Flask
from module_1.products_api import products_blueprint
from module_2.models import models
from module_3.general import general
from module_4.core import core

app = Flask(__name__)

app.register_blueprint(models, url_prefix='/models')
app.register_blueprint(general, url_prefix='/general')
app.register_blueprint(core, url_prefix='/core')
app.register_blueprint(products_blueprint, url_prefix='/products')

@app.route('/')
def basic():
    return 'Hello World !'

    
if __name__ == '__main__':
    app.run()