from flask import Blueprint ,render_template, request , flash,redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)
@auth.route('/Adlogin',methods=['GET','POST'])
def Adlogin():
    if request.method == 'POST':
      username = request.form.get('Username')
      password = request.form.get('password')  
      if username == 'Admin' and password == 'Admin' :
         return render_template('adminpage.html')
         
    return render_template('AdminLogin.html')