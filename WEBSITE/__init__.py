from flask import Flask , render_template
import json
from .views import views
from .auth import auth
def createapp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    
    with open('printerDetails.json','r') as f:
        printerDetails=json.load(f)
    numberOfPages=printerDetails['numberOfPages']
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app
