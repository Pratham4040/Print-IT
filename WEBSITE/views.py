from flask import Flask, render_template, Blueprint
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, IntegerField
from werkzeug.utils import secure_filename
import os,json
from wtforms import validators
import subprocess


views = Blueprint('views',__name__)



class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[validators.InputRequired()])
    submit = SubmitField("Upload File")
    numberOfPagesUser = IntegerField("Number Of pages", validators=[
                                     validators.InputRequired(), validators.NumberRange(min=1, max=10)])

@views.route('/', methods=['GET', "POST"])
def home():
    from app import app
    app.config['UPLOAD_FOLDER'] = 'static/files'
    form = UploadFileForm()
    with open('printerDetails.json', 'r') as f:
        printerDetails = json.load(f)
        numberOfPages = printerDetails['numberOfPages']
    
    if form.validate_on_submit():
        file = form.file.data  # First grab the file
        if int(form.numberOfPagesUser._value())>numberOfPages:
            return "No Pages Avaiable"
        numberOfPages-=int(form.numberOfPagesUser._value())
        printerDetails['numberOfPages'] = numberOfPages
        
        with open('printerDetails.json', 'w') as f:
            json.dump(printerDetails,f)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__))
                  ,app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  # Then save the file
        
        '''result = subprocess.run(
            ["lp", "static/files/"+secure_filename(file.filename)], stdout=subprocess.PIPE)'''

        #subprocess.run(['rm', "static/files/"+secure_filename(file.filename)])
        return render_template('done.html', numberOfPages=numberOfPages)
    return render_template('index.html', form=form)