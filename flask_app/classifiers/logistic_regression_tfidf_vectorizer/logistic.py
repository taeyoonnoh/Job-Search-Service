import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pickle

# 3점 이상이면 1 / 미만이면 0
def check(grade) :
  if grade >= 3.0 :
    return 1
  else :
    return 0

def regressor() :
    df = pd.read_csv('https://raw.githubusercontent.com/taeyoonnoh/Job-Search-Service/main/jasoseol.csv')

    # 자기소개서 없는 데이터 제거하기
    remove_index = df[df['자기소개서']=='0'].index.tolist()
    df = df.drop(remove_index,axis=0)

    # label 값
    df['자기소개서 평점'] = df['자기소개서 평점'].apply(check)

    # X / y 데이터 나누기
    X = df.copy()
    y = X.pop('자기소개서 평점')

    # 데이터 Sampling
    X_train,X_test,y_train,y_test = train_test_split(X,y,stratify=y,train_size=0.80)

    # 자기소개서 vector 화 시키기
    vectorizer = TfidfVectorizer()

    # Train / Test 분리
    X_train = vectorizer.fit_transform(X_train['자기소개서']).toarray()
    X_test = vectorizer.transform(X_test['자기소개서']).toarray()


    # Label 값 int 로 바꿔주기
    def toint(df) :
        return int(df)

    y_train =  y_train.apply(toint)
    y_test = y_test.apply(toint)
    
    logistic = LogisticRegression(random_state=42)

    logistic.fit(X_train,y_train)

    return logistic,vectorizer

logistic,vectorizer = regressor()

Pkl_Filename1 = "best_classifier.pkl"  

with open(Pkl_Filename1, 'wb') as file:  
    pickle.dump(logistic, file)

Pkl_Filename2 = "best_vectorizer.pkl"  

with open(Pkl_Filename2, 'wb') as file:  
    pickle.dump(vectorizer, file)