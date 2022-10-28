from flask import Blueprint,request, render_template
from flask_login import login_required, current_user
import numpy as np
import pickle
import smtplib

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

model = pickle.load(open('model_pkl', 'rb'))
def predict():
    #For rendering results on HTML GUI
    name = request.form['Full name']
    email = request.form['Email id']
    age = request.form['Age']
    
    final_features = np.zeros((29,))
    #final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction)
    # output = '{0:.{1}f}'.format(10*prediction[0][1],2)
    
    # SUBJECT = 'Reg diabetes prediction by DiaDictor'
    # TEXT = predictText + "\n" + content + "For further reference visit our webpage https://github.com/amankumar11/Diadictor\nThanks\nRegards\nDiadictor team"
    # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login("Diadictor@gmail.com", "zjyiqqmrkoznqarr")
    # server.sendmail("Diadictor@gmail.com", email, message)
    
    return render_template('result.html')