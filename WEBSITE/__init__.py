from flask import Flask , render_template
import json
from .views import views
def createapp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    
    with open('printerDetails.json','r') as f:
        printerDetails=json.load(f)
    numberOfPages=printerDetails['numberOfPages']
    app.register_blueprint(views,url_prefix='/')
    return app
