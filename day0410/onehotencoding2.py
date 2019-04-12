import numpy as np
import pandas as pd

# 연습) adult.data.txt를 읽어들여 연봉을 결정하는 중요한 7개의 속성으로만 추립니다.
# 숫자속성을 제외하고 one-hot encoding으로 변경하여 생성된 컬럼을 확인해 봅니다.
# 7개의 속성 ==> 나이,직업분류,학력,성별,주당일하는시간,직업,수입

names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
         'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']

data = pd.read_csv('../Data/adult.data.txt',header=None, names=names)
data = data[['age','workclass','education','sex','race','hours-per-week','occupation','income']]

new_df = pd.get_dummies(data)

x = new_df.loc[:,'age':'sex_ Male']
y = new_df.loc[:,'income_ >50K']

# -2 하면 맨 마지막 2개를 제외한다.
x1 = new_df.iloc[:,:-2]
y1 = new_df.iloc[:,-1]

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

lr.fit(train_x,train_y)

# 실 데이터를 적용시켜봅니다.
# 47, Private, Prof-school, Female, 60, Honduras, >50K
# 'age','workclass','education','sex','hours-per-week','occupation','income'
# 연습) 위 데이터를 예측시켜 결과를 확인해 봅니다

print(lr.score(train_x,train_y))

# 알고자하는 데이터를 훈련시킨 속성의 수와 동일하게 하기위하여 원래 원본데이터를 맨 마지막에 추가시키고 one-hot Encodeing을 합시다.
# test에는 income에 들어간 값은 임의의 값을 넣어준것.
# dummies로 만들어야하기때문에 일단 넣어준다.(속성의 개수와 값의 개수가 맞아야지 dummy 데이터로 만들 수 있기때문)
test = [[47, ' Private', ' Prof-school', ' Female',' White', 60, ' Prof-specialty',' <=50K']]

# test의 속성 하나하나가 뭔지 명시해주기(컬러명 명시)
test_df = pd.DataFrame(test, columns=['age','workclass','education','sex','race','hours-per-week','occupation','income'])

# 행을 추가하기위해 이차원 배열로 만든다.
# data = data.append(test_df)
print(data.iloc[-1,:])
'''
age                         47
workclass              Private
education          Prof-school
sex                     Female
race                     White
hours-per-week              60
occupation            Honduras
income                   <=50K
Name: 0, dtype: object

# index 값이 0으로 들어가는데 마지막에 있는 속성으로
index 값으로 가져오지 않고 마지막 값으로 가져올거기 때문에
일단 무시하기로 한다.
'''

data2 = data.append(test_df)
one_hot_data2 = pd.get_dummies(data2)

print(len(one_hot_data2.columns))
# print(one_hot_data2.columns)
print(len(new_df.columns))
# print(new_df.columns)
print(one_hot_data2)
# 똑같은 속성을 만들기위해서 행 맨 뒤에서 2번째까지
pre_x = np.array(one_hot_data2.iloc[-1,:-2]).reshape(1,-1)
print(pre_x)
'''
[[47 60  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
   0  1  0  1  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  1  0  0  0
   0]]
'''
pre_y = lr.predict(pre_x)
print(pre_y)
'''
[1]
# 1이 나오면 5만달라 이상 버는것
  0이 나오면 5만달라 미만으로 버는것
'''






















