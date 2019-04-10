import numpy as np
import pandas as pd

# 인구조사 데이터를 근거하여 소득이 연봉 50000달러 이상이 되는지 예측해보자
names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
         'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']

# data안에 columns에 names를 넣겠다~
data = pd.read_csv('../Data/adult.data.txt',header=None, names=names)

# income이 답임.
data = data[['age','workclass','education','sex','hours-per-week','occupation','income']]
# print(data.head())

# 연습) 직업분류의 종류는 모두 몇가지인지 출력
workclass_cnt = data['workclass'].unique()
print(workclass_cnt)
print(len(workclass_cnt))
'''
[' State-gov' ' Self-emp-not-inc' ' Private' ' Federal-gov' ' Local-gov'
 ' ?' ' Self-emp-inc' ' Without-pay' ' Never-worked']
9
'''

# 연습) 직업의 종류는 모두 몇가지인지 출력
occupation_cnt = data['occupation'].unique()
print(occupation_cnt)
print(len(occupation_cnt))
'''
[' Adm-clerical' ' Exec-managerial' ' Handlers-cleaners' ' Prof-specialty'
 ' Other-service' ' Sales' ' Craft-repair' ' Transport-moving'
 ' Farming-fishing' ' Machine-op-inspct' ' Tech-support' ' ?'
 ' Protective-serv' ' Armed-Forces' ' Priv-house-serv']
15
'''

# 연습) 학력의 종류 몇가지
education_cnt = data['education'].unique()
print(education_cnt)
print(len(education_cnt))
'''
[' Bachelors' ' HS-grad' ' 11th' ' Masters' ' 9th' ' Some-college'
 ' Assoc-acdm' ' Assoc-voc' ' 7th-8th' ' Doctorate' ' Prof-school'
 ' 5th-6th' ' 10th' ' 1st-4th' ' Preschool' ' 12th']
16
'''

# 연습) 성별의 종류 모두 몇가지 인지
sex_cnt = data['sex'].unique()
print(sex_cnt)
print(len(sex_cnt))
'''
[' Male' ' Female']
2
'''

# 연습) 수익의 종류 모두 몇가지 인지
income_cnt = data['income'].unique()
print(income_cnt)
print(len(income_cnt))
'''
[' <=50K' ' >50K']
2
'''

# 연습) 50000달라 이상인 사람은 모두 몇명?
income_50 = data[data['income'] == ' >50K']
print(len(income_50))
'''
7841
'''

# 연습) 여자중에 5만달러 이상인 사람 몇명 ?
Femail_income_50 = income_50[income_50['sex'] == ' Female']
# print(Femail_income_50)
print(len(Femail_income_50))
'''
1179
'''

# 연습) 5만달러 이상인 사람들의 평균 나이는 몇살 ?
mean_age = income_50.pivot_table(values='age', index='income', aggfunc='mean')
print(mean_age)
'''
44.249841
'''

# 가장많은 직업군은 ?
occupation_max = data.pivot_table(values='age', index='occupation', aggfunc='count').sort_values(by='age',ascending=False)
print(occupation_max.head(1))
'''
 Prof-specialty  4140
'''

# 가장 많은 학력은 ?
education_max = data.pivot_table(values='income', index='education', aggfunc='count').sort_values(by='income',ascending=False)
print(education_max.head(1))
'''
 HS-grad   10501
'''
# 5만달러 이상인 직업중에 주당 일하는 시간이 가장 적은 직업군 top5는 ?
perWeek = income_50.pivot_table(values='hours-per-week', index='occupation', aggfunc='mean').sort_values(by='hours-per-week',ascending=True)
print(perWeek.head(5))
'''
                  hours-per-week
occupation                      
 Priv-house-serv       35.000000
 ?                     36.146597
 Armed-Forces          40.000000
 Adm-clerical          40.942801
 Tech-support          41.427562
'''