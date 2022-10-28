from django.shortcuts import render
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

@views.route('/result')
def result():
    return render_template("result.html")


model = pickle.load(open('model_pkl', 'rb'))


def predict():
    #For rendering results on HTML GUI
    name = request.form['Full name']
    email = request.form['Email id']
    age = request.form['Age']
    dict={'itching':0,'skin_rash':0,'chills':0,'joint_pain':0,'vomiting':0,'fatigue':0,'weight_loss':0,'lethargy':0,'cough':0,'high_fever':0,'breathlessness':0,'head_ache':0,'yellowish_skin':0,'dark_urin':0,'nausea':0,'loss_of_appetite':0,'abdominal_pain':0,'diarrhoea':0,'mild_fever':0,'yellowing_of_eyes':0,'swelled_lymph_nodes':0,'malaise':0,'blurred_and_distorted_vision':0,'phlegm':0,'chest_pain':0,'dizziness':0,'stiff_neck':0,'loss_of_balance':0,'muscle_pain':0}

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