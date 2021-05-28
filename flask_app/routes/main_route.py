from flask import Blueprint, render_template, request,redirect,url_for
from flask_app import db
from flask_app.models.jobs import Job
from flask_app.models.quotes import Quotes
import random
from flask_app.utils.functions import get_quotes,get_gongo

bp = Blueprint('main', __name__)

@bp.route('/', methods=['POST', 'GET'])
def index():
    
    try : 
        all_jobs =  db.session.query(Job).all()
        db.session.delete(all_jobs)
        db.session.commit()
    
    except:
        pass


    # 명언 데이터베이스
    quotes = db.session.query(Quotes).first()

    if quotes :
        pass

    else :
        for i in get_quotes() :
            add_quotes = Quotes(quotes_text=i)
            db.session.add(add_quotes)
            db.session.commit()

    rand = random.randrange(0, db.session.query(Quotes).count()) 
    row = db.session.query(Quotes)[rand]

    if request.method=='POST' :
        company_name = request.form['company_name']
        if not company_name :
            return redirect(url_for("main.index"))
        return redirect(url_for("main.add_gongo", company_name=company_name, quote=row))

    return render_template("first_page.html",quote=row)

@bp.route('/add/<company_name>', methods=['GET','POST'])
def add_gongo(company_name):
    rand = random.randrange(0, db.session.query(Quotes).count()) 
    row = db.session.query(Quotes)[rand]

    company = db.session.query(Job).filter(Job.keyword==company_name).first()

    # DB 에 해당 회사명으로 조회한 회사의 공고가 없을 경우 DB에 추가
    if company is None :
        job_title, study_period, experience, money, job_app, area, job_end, field, spec_work, apply_company_name, keyword, links = get_gongo(str(company_name))
        for i in range(len(job_title)) : 
            db.session.add(Job(
                job_title=job_title[i],
                study_period=study_period[i],
                experience=experience[i],
                money=money[i],
                job_app=job_app[i],
                area=area[i],
                job_end=job_end[i],
                field=field[i],
                spec_work=spec_work[i],
                company_name=apply_company_name[i],
                keyword= str(company_name),
                links=str(links[i])
            ))
            db.session.commit()

    job_list = db.session.query(Job).all()

    query = db.session.query(Job.keyword.distinct().label("keyword"))
    distinct_keywords = [row.keyword for row in query.all()]

    if request.method=='POST' :
        company_name = request.form['company_name']

        return redirect(url_for("main.add_gongo", company_name=company_name, quote=row, job_list=job_list, distinct_keywords=distinct_keywords))

    return render_template("first_page.html", job_list=job_list, quote=row, company_name=company_name, distinct_keywords=distinct_keywords)

@bp.route('/delete/<keyword>', methods=['GET','POST'])
def delete_gongo(keyword=None):
    delete_keyword = db.session.query(Job).filter(Job.keyword==keyword).all()

    for i in delete_keyword :
        db.session.delete(i)
        db.session.commit()

    rand = random.randrange(0, db.session.query(Quotes).count()) 
    row = db.session.query(Quotes)[rand]

    job_list = db.session.query(Job).all()

    query = db.session.query(Job.keyword.distinct().label("keyword"))
    distinct_keywords = [row.keyword for row in query.all()]

    if request.method=="POST" :
        company_name = request.form['company_name']
        return redirect(url_for("main.add_gongo", company_name=company_name, quote=row))

    return render_template("first_page.html", quote=row, job_list=job_list, distinct_keywords=distinct_keywords)