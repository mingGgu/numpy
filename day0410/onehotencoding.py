import numpy as np
import pandas as pd

# 연습) adult.data.txt를 읽어들여 연봉을 결정하는 중요한 7개의 속성으로만 추립니다.
# 숫자속성을 제외하고 one-hot encoding으로 변경하여 생성된 컬럼을 확인해 봅니다.
# 7개의 속성 ==> 나이,직업분류,학력,성별,주당일하는시간,직업,수입

names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
         'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']

data = pd.read_csv('../Data/adult.data.txt',header=None, names=names)
data = data[['age','workclass','education','sex','hours-per-week','occupation','income']]
# print(data.columns)

# 위의 데이터프레임을 one-hot 을 하면 몇개의 속성이 생성될까요
# workclass 의 값의 종류의 수
# education 의 값의 종류의 수
# sex 의 값의 종류의 수
# hours-per-week 의 값의 종류의 수
# occupation 의 값의 종류의 수
# income 의 값의 종류의 수

print(len(data['workclass'].unique()))
print(len(data['education'].unique()))
print(len(data['occupation'].unique()))
print(len(data['sex'].unique()))
print(len(data['income'].unique()))
'''
9
16
15
2
2

각 컬럼의 숫자를 제외한 문자속성인 컬럼의 값의 종류의 수 만큼 컬럼이 생성된다.
age와 hours-per-week 에 들어있는 속성은 숫자라서 컬럼수에 하나씩만 더해 줌
각 컬럼의 수는 위에서 출력한 값이 나오고 이 값을 다 더한 값이 one-hot Encoding 한 값이다
9+16+15+2+2+1(age)+1(hours-per-week) = 46개 만들어진다. 
'''

new_df = pd.get_dummies(data)
# print(new_df.head())
'''
   age  hours-per-week  ...  income_ <=50K  income_ >50K
0   39              40  ...              1             0
1   50              13  ...              1             0
2   38              40  ...              1             0
3   53              40  ...              1             0
4   28              40  ...              1             0

[5 rows x 46 columns]
'''
# print(new_df.columns)

# 학습을 시키려면 갖고있는 데이터로 부터 문제와 답을 분리한다.
# 여기선 맨 마지막 속성인 income이 답인데 답이 두가지( <=50K, >50K ) 이므로 하나를 정해줌
# 수입이 5만달라 이상인것 을 정답으로 할것이다. ( >50K)
# 그래서 수입이 5만달라가 아니면 0 맞으면 1로 처리한다.

# 연습) 문제와 답을 분리하여 각각 x와 y에 넣는다.

# fancy indexing
# 2차원 배열인 경우 원하는 데이터를 추출하기 위하여 행열을 분리하여 범위를 지정해 slicing할 수 있다.
# 데이터프레임[행, 열]
# pandas에 데이터프레임의 slicing을 위해서는 loc, iloc을 쓴다.

x = new_df.loc[:,'age':'sex_ Male']
y = new_df.loc[:,'income_ >50K']
# print(x.columns)
'''
0    0
1    0
2    0
3    0
4    0
'''

print(y.head())
'''
Name: income_ >50K, dtype: uint8
'''
# -2 하면 맨 마지막 2개를 제외한다.
x1 = new_df.iloc[:,:-2]
y1 = new_df.iloc[:,-1]
# print(x1.columns)
'''
0    0
1    0
2    0
3    0
4    0
'''
# print(y1.head())
'''
Name: income_ >50K, dtype: uint8
'''

# 문제와 답의 차수 확인
# print(x1.shape)      #(32561, 44)
# print(y1.shape)      #(32561,)

from sklearn import linear_model,model_selection

# 문제x와 답y를 훈련에 참여시킬 데이터와 검증을 위한 데이터로 분리한다.
train_x, test_x, train_y, test_y = model_selection.train_test_split(x1,y1)

print(len(train_x), len(train_y))
'''
24420 24420
'''

print(len(test_x), len(test_y))
'''
8141 8141
'''

lr = linear_model.LogisticRegression()
# fit은 학습시키는거. train_x는 문제, train_y는 답 이 두가지를 가지고 훈련시킨다.
lr.fit(train_x,train_y)
# r에 한번 알아맞혀봐~ 하고 predict를 통해 예측하게한다.
r = lr.predict(test_x)
# 예측연습해본 r의 답과 진짜답(test_y)을 비교해서 맞는지 확인 : r의 개수와 test_y의 개수를 비교
print(len(r))
print(len(test_y))
'''
8141
8141
# 동일하게 나옴
'''

# 예측한 결과 r과 검증을 위한 진짜답 test_y를 서로 비교합니다.
result  = r == test_y
# boolean array로 출력
print(result)
# 검증한 결과가 Series라서 value만 뽑아본다.
a = result.values
# True인것만 추출
b = a[a == True]
print(len(b))
'''
6580
'''
print('정답률:',len(b)/len(test_y)*100)
'''
정답률: 80.92371944478566
'''

print('정답률:',lr.score(test_x,test_y))
'''
정답률: 0.8152561110428694
'''