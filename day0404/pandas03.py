import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/scores.csv')

# pandas의 DataFrame에서 행에 접근하는 방법은 loc 이나 iloc 함수를 이용하여 접근한다.
# key값을 부여하지 않고 행에 접근하려면 index로 접근합니다.
# 이때는 loc나 iloc을 사용하는데에 차이가 없다. 그러나 key값을 부여했을때는 달라짐
# index로 접근할 때는 iloc을 사용
# key로 접근할 때는 loc을 사용

print(df.loc[2].values)
print(df.iloc[2].values)
'''
[1 'ben' 95 59 96 88]
[1 'ben' 95 59 96 88]
'''














# 내손으로 dataframe만들기
# df = pd.DataFrame([[1,2,3],[4,5,6]])
# print(df)
# print(type(df))
'''
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# <class 'pandas.core.frame.DataFrame'>
# # 보통은 파일의 내용을 읽어들여서 dataframe을 만든다.
# '''
# #
# # #파일 열기(읽어들이기)
# # # 직접 ,를 구분안해도 되고 알아서 csv를 읽어들이는 함수
# # df = pd.read_csv('Data/scores.csv')
# # print(df)
# # print(type(df))
# # '''
# #     class    name  kor  eng  mat  bio
# # 0       1    adam   67   87   90   98
# # 1       1  andrew   45   45   56   98
# # 2       1     ben   95   59   96   88
# # 3       1   clark   65   94   89   98
# # 4       1     dan   45   65   78   98
# # 5       1    noel   78   76   98   89
# # 6       2    paul   87   67   65   56
# # 7       2  walter   89   98   78   78
# # 8       2   oscar  100   78   56   65
# # 9       2  martin   99   89   87   87
# # 10      2    hugh   98   45   56   54
# # 11      2   henry   65   89   87   78
# #
# # ↑
# # key의 역할
# #
# # <class 'pandas.core.frame.DataFrame'>
# # '''
# #
# # print(df.index)
# # '''
# # RangeIndex(start=0, stop=12, step=1)
# # # index를 확인할 수 있다.
# # '''
# #
# # print(df.columns)
# # '''
# # Index(['class', 'name', 'kor', 'eng', 'mat', 'bio'], dtype='object')
# # # 컬럼명들을 확인
# # '''
# #
# # print(df.values)
# # print(type(df.values))
# # '''
# # [[1 'adam' 67 87 90 98]
# #  [1 'andrew' 45 45 56 98]
# #  [1 'ben' 95 59 96 88]
# #  [1 'clark' 65 94 89 98]
# #  [1 'dan' 45 65 78 98]
# #  [1 'noel' 78 76 98 89]
# #  [2 'paul' 87 67 65 56]
# #  [2 'walter' 89 98 78 78]
# #  [2 'oscar' 100 78 56 65]
# #  [2 'martin' 99 89 87 87]
# #  [2 'hugh' 98 45 56 54]
# #  [2 'henry' 65 89 87 78]]
# # <class 'numpy.ndarray'>
# # '''
# #
# # # 국어점수만 뽑고싶다.
# # print(df['kor'])
# # # print(df[2])  #불가능 2번째 행출력 X , 2번째 열출력 X 오류난다.
# # '''
# # 0      67
# # 1      45
# # 2      95
# # 3      65
# # 4      45
# # 5      78
# # 6      87
# # 7      89
# # 8     100
# # 9      99
# # 10     98
# # 11     65
# # Name: kor, dtype: int64
# '''



