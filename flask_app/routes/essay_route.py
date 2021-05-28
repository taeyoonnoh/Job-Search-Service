from flask import Blueprint, render_template, request
import numpy as np
import pickle
from flask_app.models.pickle import Classifier
from flask_app import db

bp = Blueprint('essay', __name__)

@bp.route('/', methods=['GET','POST'])
def move_to_essay_page():

    my_grade= None

    if request.method=='POST' : 

        essay_texts = request.form['essay_texts']

        Pkl_Filename1 = "best_classifier.pkl"  
        Pkl_Filename2 = "best_vectorizer.pkl"  

        with open(Pkl_Filename1, 'rb') as file:  
            classifier = pickle.load(file)

        with open(Pkl_Filename2, 'rb') as file:  
            vectorizer = pickle.load(file)

        a = vectorizer.transform([essay_texts]).toarray()
        my_grade = np.round(classifier.predict_proba(a)[0][1] * 100,2)

        return render_template("third_page.html", my_grade=my_grade)
    

    return render_template("third_page.html", my_grade=my_grade)