from flask import Blueprint, render_template, request,redirect,url_for
from flask_app.models.news import News
from flask_app import db
from flask_app.utils.functions import get_news

bp = Blueprint('news', __name__)

@bp.route('/', methods=['GET','POST'])
def move_to_news_page():

    news = db.session.query(News).all()

    try :
        query = db.session.query(News.searched_keyword.distinct().label("keyword"))
        distinct_keywords = [row.keyword for row in query.all()]

    except :
        pass

    if request.method=="POST" : 
        search = request.form['search_word']
        if not search :
            return redirect(url_for("news.move_to_news_page"))
        return redirect(url_for("news.add_news",search=search))
        
    return render_template("second_page.html", news=news, distinct_keywords=distinct_keywords)

@bp.route('/add_news/<search>', methods=['GET','POST'])
def add_news(search):   
    check_search_in_db = db.session.query(News).filter(News.searched_keyword==search).first()

    if check_search_in_db : 
        return redirect(url_for("news.move_to_news_page"))

    title, url_list, summarized_text, keyword_list = get_news(search)

    for i in range(len(title)) :
        db.session.add(News(
            news_title=title[i],
            news_summarized=summarized_text[i],
            searched_keyword=keyword_list[i],
            url_link=url_list[i],
        ))
        db.session.commit()            

    return redirect(url_for("news.move_to_news_page"))

@bp.route('/delete_news/<keyword>', methods=['GET','POST'])
def delete_news(keyword=None):
    delete_keyword = db.session.query(News).filter(News.searched_keyword==keyword).all()

    for i in delete_keyword :
        db.session.delete(i)
        db.session.commit()

    return redirect(url_for("news.move_to_news_page"))