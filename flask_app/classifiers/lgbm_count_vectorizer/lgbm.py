import pandas as pd
import numpy as np
from lightgbm import LGBMClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# 3점 이상이면 1 / 미만이면 0
def check(grade) :
  if grade >= 3.0 :
    return 1
  else :
    return 0

def regressor() :
    df = pd.read_csv('https://raw.githubusercontent.com/taeyoonnoh/Job-Search-Service/main/jasoseol.csv')

    df['새로운 평점'] = df['자기소개서 평점'].apply(check)

    # 자기소개서 없는 데이터 제거하기
    remove_index = df[df['자기소개서']=='0'].index.tolist()
    df = df.drop(remove_index,axis=0)

    df = df.drop('자기소개서 평점',axis=1)

    # 데이터 sampling
    test_df = df.sample(frac=0.2, random_state=42)
    remove_index = test_df.index.tolist()
    train_df = df.drop(remove_index,axis=0)

    # 자기소개서 vector 화 시키기
    vectorizer = CountVectorizer()

    a = np.array(train_df['자기소개서'])
    b = np.array(test_df['자기소개서'])

    c = list(vectorizer.fit_transform(a).toarray())
    d = list(vectorizer.transform(b).toarray())

    train_df['자기소개서'] = c
    test_df['자기소개서'] = d

    # Train / Test Data Split
    y_train = train_df['새로운 평점']
    X_train = train_df.drop("새로운 평점", axis=1)

    y_test = test_df['새로운 평점']
    X_test = test_df.drop("새로운 평점", axis=1)

    # Label 값 int 로 바꿔주기
    def toint(df) :
        return int(df)

    y_train =  y_train.apply(toint)
    y_test = y_test.apply(toint)
    
    lgbmc = LGBMClassifier(objective='binary',n_jobs=-1,random_state=42,base_score=0.2054675960421993)

    lgbmc.fit(list(X_train['자기소개서']),y_train)

    return lgbmc,vectorizer

lgbmc,vectorizer = regressor()

Pkl_Filename1 = "best_classifier.pkl"  

with open(Pkl_Filename1, 'wb') as file:  
    pickle.dump(lgbmc, file)

Pkl_Filename2 = "best_vectorizer.pkl"  

with open(Pkl_Filename2, 'wb') as file:  
    pickle.dump(vectorizer, file)