# from crypt import methods
from bs4 import Doctype
from django.shortcuts import render
from flask import Blueprint,request, render_template
from flask_login import login_required, current_user
import numpy as np
import pickle
import smtplib
from . import db
from .models import User

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

@views.route('/result', methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    symptoms = request.form.getlist('symptoms[]')
    # print(symptoms)
    # final_features = np.array([symptoms])
    # print(final_features)
    dict={'itching':0,'skin_rash':0,'chills':0,'joint_pain':0,'vomiting':0,'fatigue':0,'weight_loss':0,'lethargy':0,'cough':0,'high_fever':0,'breathlessness':0,'head_ache':0,'yellowish_skin':0,'dark_urin':0,'nausea':0,'loss_of_appetite':0,'abdominal_pain':0,'diarrhoea':0,'mild_fever':0,'yellowing_of_eyes':0,'swelled_lymph_nodes':0,'malaise':0,'blurred_and_distorted_vision':0,'phlegm':0,'chest_pain':0,'dizziness':0,'stiff_neck':0,'loss_of_balance':0,'muscle_pain':0}
    for s in symptoms:
        dict[s]=1
    final_features = list(dict.values())
    # print(final_features)
    
    # final_features = np.zeros((29,))
    # final_features = [np.array(int_features)]
    # final_features.reshape(1,-1)
    prediction = model.predict([final_features])

    # doc = User.query.filter_by(doctype=prediction).all()
    # print(doc.name)

    # docs = User.query.all()

    # for doc in docs:
    #     print(doc.name)

    # print(prediction)
    
    # output = '{0:.{1}f}'.format(10*prediction[0][1],2)
    predictText="Greetings from WeCare\nOn the basis of the information provided by you, our predictor has found that you are at the risk of you having "+prediction[0]
    SUBJECT = 'Reg disease prediction by Wecare'
    TEXT = predictText + "\n" +  "For further reference visit our webpage"+"\n"+"Note: This is just a prediction and not a real diagnosis of the disease. You should consult a doctor immediately if you feel you are at risk." 
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("wecareforyou365247@gmail.com", "kpufeafxhrgenvpq")
    server.sendmail("wecareforyou365247@gmail.com", email, message)
    
    return render_template('result.html', prediction = prediction[0])