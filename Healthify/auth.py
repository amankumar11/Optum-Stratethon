from crypt import methods
from xmlrpc.client import boolean
from flask import Blueprint, flash, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("signin.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif len(name) < 2:
            flash("Name must be greater than 2 characters.", category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            flash("Account created", category='success')
            # add user to db 
            pass
    return render_template("signup.html")