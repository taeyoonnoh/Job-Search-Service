import requests
from bs4 import BeautifulSoup
from gensim.summarization.summarizer import summarize
import re

# get_page
def get_page(page_url) : 

    req = requests.get(page_url)

    soup = BeautifulSoup(req.content, "html.parser")

    return soup

# get quotes
def get_quotes() :
    url = 'https://heartsaying.com/archives/3974'

    soup = get_page(url)

    a = soup.find_all("p")

    text_list = []
    for i in a :
        text_list.append(i.text)
    
    edited_text_list = text_list[2:50]

    for i in range(10) :
        edited_text_list[i] = edited_text_list[i][3:]

    for i in range(10,48) : 
        edited_text_list[i] = edited_text_list[i][4:]

    return edited_text_list

# get gongo
def get_gongo(name) :
    base_url = 'http://api.saramin.co.kr/job-search/rss?keywords='
    end_url = '&edu_lv=3'
    soup = get_page(base_url+name+end_url)

    a = soup.find_all("item")

    text_list = []

    for i in a :
        text_list.append(i.text)

    b = re.split('<[^<>]+>',str(text_list))

    job_title = []
    study_period = []
    experience = []
    money=[]
    job_app = []
    area = []
    job_end = []
    field = []
    spec_work = []
    company_name = []
    keyword = []

    for i in range(len(b)) :
        if b[i]=='공고명:' :
            job_title.append(b[i+1])
        if b[i]=='학력:' :
            study_period.append(b[i+1])
        if b[i]=='경력:' :
            experience.append(b[i+1])
        if b[i]=='연봉:' :
            money.append(b[i+1])
        if b[i]=='고용형태:' :
            job_app.append(b[i+1])
        if b[i]=='근무지역:' :
            area.append(b[i+1])
        if b[i]=='마감일:' :
            job_end.append(b[i+1])
        if b[i]=='산업/업종:' :
            field.append(b[i+1])
        if b[i]=='직업/직종:' :
            spec_work.append(b[i+1])
        if b[i]=='기업명:' :
            company_name.append(b[i+1])
        keyword.append(name)
        
    links = []
    for i in text_list :
        links.append(str(i).split('\n')[2])

    return job_title, study_period, experience, money, job_app, area, job_end, field, spec_work, company_name, keyword, links

# get news info
def get_news(keyword) : 
    url = f'http://www.inews24.com/search/?sort=new&word={keyword}&sec=tc&period=month&s_date=&e_date='
    soup = get_page(url)

    a = soup.find_all('h1')
    keyword_list = []
    title=[]
    for i in a :
        title.append(i.text)
        keyword_list.append(keyword)

    url_list = []
    base_url = 'http://www.inews24.com'

    for i in soup.find_all("a",href=True) :
        if str(i['href']).startswith("/view") :
            url_list.append((base_url+str(i['href'])))

    total_contents=[]

    for i in url_list :
        small_content=[]
        soup = get_page(i)
        a = soup.find_all("p")
    
        for j in range(len(a)-2) :
            small_content.append(a[j].text)
        total_contents.append(small_content)

    summarized_text = summarizer(total_contents)

    return title, url_list, summarized_text, keyword_list

def summarizer(total_contents) : 
    summarize_list = []
    text=''
    for i in total_contents:
        for j in i :
            text +=j
        text=text.replace(".",". ")
        summarized_text = summarize(text,ratio=0.25,split=False,word_count=30)
        edited_text = summarized_text.replace("다.","다.\n\n")
        summarize_list.append(edited_text)
        text=''

    return summarize_list

