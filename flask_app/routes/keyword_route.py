from flask import Blueprint, render_template, request,redirect,url_for
from flask_app.models.essay import Essay
from flask_app import db
import pandas as pd

bp = Blueprint('keyword', __name__)

@bp.route('/', methods=['GET','POST'])
def move_to_check_essay_page():
    essays = db.session.query(Essay).all()

    try :
        query = db.session.query(Essay.company_name.distinct().label("company_name"))
        distinct_keywords = [row.company_name for row in query.all()]

        common_words_dict = {}
        for i in distinct_keywords :
            common_words_dict[i] = db.session.query(Essay.keyword).filter(Essay.company_name==i).first()

    except :
        pass

    if request.method=="POST" : 
        keyword = request.form['keyword']
        if not keyword  :
            return redirect(url_for("keyword.move_to_check_essay_page"))

        return redirect(url_for("keyword.add_keyword", keyword=keyword))
    
    return render_template("forth_page.html", distinct_keywords=distinct_keywords, essay=essays, common_words=common_words_dict)

@bp.route('/add_keyword/<keyword>', methods=['GET','POST'])
def add_keyword(keyword):   
    check_if_exists = db.session.query(Essay).filter(Essay.company_name==keyword).first()

    if check_if_exists :
        return redirect(url_for("keyword.move_to_check_essay_page"))
    
    df = pd.read_csv('https://raw.githubusercontent.com/taeyoonnoh/Job-Search-Service/main/jasoseol.csv')
    df1 = df[df['회사명'].str.contains(str(keyword))]

    df2 = pd.read_csv('https://raw.githubusercontent.com/taeyoonnoh/Job-Search-Service/main/keyword.csv')
    for i in df1.index.tolist() :
        db.session.add(Essay(
            company_name=df1['회사명'][i],
            essays=df1['자기소개서'][i],
            url_link = df1['링크'][i],
            grade = df1['자기소개서 평점'][i],
            keyword = str(df2[df2['회사명']==df1['회사명'][i]]['공통 키워드'].values[0])[2:-2]
        ))
        db.session.commit()

    essays=db.session.query(Essay).all()

    return redirect(url_for("keyword.move_to_check_essay_page"))

@bp.route('/delete_keyword/<keyword>', methods=['GET','POST'])
def delete_keyword(keyword=None):
    delete_keyword = db.session.query(Essay).filter(Essay.company_name==keyword).all()

    for i in delete_keyword :
        db.session.delete(i)
        db.session.commit()

    return redirect(url_for("keyword.move_to_check_essay_page"))