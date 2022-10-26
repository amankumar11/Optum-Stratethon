from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("doctor_dashboard.html", user=current_user)