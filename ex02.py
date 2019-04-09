# 연습) Data폴더의 users.dat. movies.dat, ratings.dat 파일을 읽어들여 하나의 DataFrame으로 만들어 봅니다.
import numpy as np
import pandas as pd

# 평가한 시험의 수가 500건 이상인 영화를 건수를 기준으로 내림차순 정렬하여 반환
def get_500_movie():

    df = getMovie()
    title_count = df.pivot_table(values='userid', index='title', aggfunc='count')
    title_500 = title_count[title_count['userid'] >= 500]
    title_500_sort = title_500.sort_values(by='userid', ascending=False)
    return title_500_sort


# 3개의 파일(movies, users, ratings)을 하나의 데이터프레임으로 반환하는 함수
def getMovie():

    movies = pd.read_csv('../ml-1m/movies.dat',sep='::',engine='python',header=None, names=['movieid','title','ganre'])
    ratings = pd.read_csv('../ml-1m/ratings.dat',sep='::',engine='python',header=None, names=['userid','movieid','rating','timestamp'])
    users = pd.read_csv('../ml-1m/users.dat',sep='::',engine='python',header=None, names=['userid','gender','age','jop','zipcode'])
    df = pd.merge( pd.merge(ratings,movies),users)
    return  df

