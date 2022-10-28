from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/form')
def form():
    return render_template("predict_form.html")

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("doctor_dashboard.html", user=current_user)

@views.route('/result')
def result():
    return render_template('result.html')