# Job-Search-Service

<br/>

## Web Application
### [Job Search Service][link]

[link]:https://job-searching-service.herokuapp.com/

<br/>

## Project Information
* 취업준비생을 위한 서비스 구현
* Flask 로 기능 구현 & Heroku 로 배포

<br/>

## Setups
* python version : 3.7.10
* `pip install -r requirements.txt`

**Development Mode (로컬에서 구동할 때 아래와 같이 입력)**
* `export FLASK_APP=titanic_flask`
* `export FLASK_ENV=development`
* `flask run`

<br/>

**Production Mode (웹에서 구동할 때 아래와 같이 입력)**
* `export FLASK_APP=titanic_flask`
* `export FLASK_ENV=production`
* `git add .`
* `git commit -m "{commit message}"`
* `git push heroku main`

<br/>

## Folder Layout
```python
완성하고 작성할 것
```

<br/>

## Functions

1. **Dashboard**

Dashboard 페이지에서는 회사명을 치면 관련 공고 소식을 받아볼 수 있습니다.

`Update 사항 : 사람인 Open Api 서비스 종료에 따라 해당 기능 사용 불가`

2. **News**

News 페이지에서는 검색어를 입력하면 관련 뉴스를 조회할 수 있고 요약된 기사 내용을 받아볼 수 있습니다.

3. **Essay**

Essay 페이지에서는 자신이 쓴 글이 어느정도 수준이 되는 지 확인할 수 있습니다. 자신이 쓴 자기소개서를 복사 + 붙여넣기 하면 점수가 나옵니다. 여기서 점수가 높을수록 잡코리아의 전문가한테서 평가를 받았을 때 3점 이상일 가능성이 높다는 것을 의미합니다. 

4. **Keyword**

Keyword 페이지에서는 회사명을 입력하면 해당 회사의 모든 합격 자기소개서에 어떤 단어의 빈도수가 높은 지 확인할 수 있습니다. 그리고 지원할 회사의 모든 합격 자기소개서 데이터를 받아볼 수 있습니다.

<br/>

## 합격 자기소개서 Data Preprocessing

**Binary Classification**
|![3](https://user-images.githubusercontent.com/74780115/119500252-8fcf2100-bda2-11eb-904c-ae9987eb2b5d.PNG "captionnnn")|
|:--:|
|3점 이상은 1 / 3점 미만은 0 으로 간주|

<br/>

## Essay Classifier Model Evaluation
|Model|Accuracy|Precision|Recall|F1-Score|Base-score|Model 적용 여부|비고|
|--|:--:|:--:|:--:|:--:|:--:|:--:|--|
|LGBM + CountVectorizer|0.67|0.60|0.60|0.60|0.205|||
|LGBM + TfidfVectorizer|0.68|0.61|0.59|0.60|0.552|:heavy_check_mark:||
|Only Nouns + LGBM + CountVectorizer|0.67|0.60|0.61|0.60|0.385||명사 추출 후 토큰화 진행|
|Only Nouns + LGBM + TfidfVectorizer|0.66|0.59|0.54|0.56|0.353||명사 추출 후 토큰화 진행|

<br/>

## Demonstration Video

<br/>

## Reference

* 합격 자기소개서 데이터 (잡코리아) - https://www.jobkorea.co.kr/starter/passassay/

<br/>

## To Do List

|To Do|On Progress|Completion|Update Date|
|--|:--:|:--:|:--:|
|iframe heroku 수정|-|-||
|pkl 파일 heroku load|-|:heavy_check_mark:|**2021-05-23**|
|다양한 ML & DL 모델 적용|:heavy_check_mark:|-||
|공고 조회 페이지 수정|-|-||
|자동 업데이트 기능 추가|-|-||
|키워드 불용어 처리|-|-||
|유사 합격 자기소개서 찾기 기능 추가|-|-||
|Multiclass Classifier 모델 구현|:heavy_check_mark:|-||
|데이터 시각화 ReadMe 추가|:heavy_check_mark:|-||
