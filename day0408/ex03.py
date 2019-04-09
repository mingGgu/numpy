import ex02
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = ex02.getMovie()
print(df)

# r = df.pivot_table(values='rating',index='gender',aggfunc='mean')
# print(r)
'''
          rating
gender          
F       3.620366
M       3.568879
'''
r = df.pivot_table(values='rating',index='gender',aggfunc='mean',columns='age')
# print (r)
'''
age           1         18       25        35        45        50        56
gender                                                                     
F       3.616291  3.453145  3.60670  3.659653  3.663044  3.797110  3.915534
M       3.517461  3.525476  3.52678  3.604434  3.627942  3.687098  3.720327
'''

r = df.pivot_table(values='rating',index='age',aggfunc='mean',columns='gender')
# print(r)
'''
gender         F         M
age                       
1       3.616291  3.517461
18      3.453145  3.525476
25      3.606700  3.526780
35      3.659653  3.604434
45      3.663044  3.627942
50      3.797110  3.687098
56      3.915534  3.720327
'''
# 배열중 먼저 오는 것이 처음 기준점이 된다.
# 여기선 age가 먼저 오기때문에 age로 나눈뒤 gender로 나눠준다

r = df.pivot_table(values='rating',index=['age','gender'],aggfunc='mean')
# print(r)
'''
              rating
age gender          
1   F       3.616291
    M       3.517461
18  F       3.453145
    M       3.525476
25  F       3.606700
    M       3.526780
35  F       3.659653
    M       3.604434
45  F       3.663044
    M       3.627942
50  F       3.797110
    M       3.687098
56  F       3.915534
    M       3.720327
'''

r2 = df.pivot_table(values='rating',index=['gender','age'],aggfunc='mean')
# print(r2)
'''
gender age          
F      1    3.616291
       18   3.453145
       25   3.606700
       35   3.659653
       45   3.663044
       50   3.797110
       56   3.915534
M      1    3.517461
       18   3.525476
       25   3.526780
       35   3.604434
       45   3.627942
       50   3.687098
       56   3.720327
'''

# 연습) 직업별, 성별, 나이대별 평균평점을 알려주세요 단 결축치는 0으로 채워주세요

job_gender_age = df.pivot_table(values='rating', index=['gender','age'], columns='jop', aggfunc='mean',fill_value=0)
print(job_gender_age)
'''
jop               0         1         2   ...        18        19        20
gender age                                ...                              
F      1    3.836493  3.919192  3.454545  ...  0.000000  2.678392  0.000000
       18   3.599043  3.365123  3.220090  ...  0.000000  3.113145  3.053462
       25   3.709261  3.521060  3.527070  ...  3.887324  3.700478  3.369403
       35   3.746459  3.647967  3.576022  ...  0.000000  3.724440  3.711206
       45   3.416619  3.592746  3.744530  ...  0.000000  0.000000  3.645475
       50   3.751445  3.832181  3.883107  ...  4.224265  0.000000  3.762648
       56   3.946942  3.855932  4.072978  ...  0.000000  0.000000  4.522388
M      1    3.602017  3.264781  3.619565  ...  0.000000  3.695216  0.000000
       18   3.430697  3.346113  3.606355  ...  3.389562  3.382344  3.442130
       25   3.455094  3.530138  3.531350  ...  3.541882  3.297287  3.463661
       35   3.604399  3.490172  3.533841  ...  3.522846  3.312796  3.555450
       45   3.373308  3.760632  3.823815  ...  3.582396  3.447826  3.281888
       50   3.438066  3.696596  3.952599  ...  3.392966  4.008646  3.788662
       56   3.948553  3.751479  3.670762  ...  3.474627  3.584488  3.960624
'''

job_age_gender = df.pivot_table(values='rating', index=['jop','age'], columns='gender', aggfunc='mean',fill_value=0)
age_gender_job = df.pivot_table(values='rating', index=['age','jop'], columns='gender', aggfunc='mean',fill_value=0)

print(job_age_gender)
'''
gender          F         M
jop age                    
0   1    3.836493  3.602017
    18   3.599043  3.430697
    25   3.709261  3.455094
    35   3.746459  3.604399
    45   3.416619  3.373308
    50   3.751445  3.438066
    56   3.946942  3.948553
1   1    3.919192  3.264781
    18   3.365123  3.346113
    25   3.521060  3.530138
    35   3.647967  3.490172
    45   3.592746  3.760632
    50   3.832181  3.696596
    56   3.855932  3.751479
2   1    3.454545  3.619565
    18   3.220090  3.606355
    25   3.527070  3.531350
    35   3.576022  3.533841
    45   3.744530  3.823815
    50   3.883107  3.952599
    56   4.072978  3.670762
3   18   3.794947  3.544400
    25   3.551240  3.602432
    35   3.797710  3.608409
'''
print(age_gender_job)
'''
gender          F         M
age jop                    
1   0    3.836493  3.602017
    1    3.919192  3.264781
    2    3.454545  3.619565
    4    0.000000  3.574661
    7    4.702703  3.566667
    8    0.000000  3.651163
    10   3.581952  3.492646
    11   0.000000  3.066667
    12   0.000000  3.309417
    13   0.000000  4.000000
    14   0.000000  3.513699
    17   0.000000  3.966102
    19   2.678392  3.695216
18  0    3.599043  3.430697
    1    3.365123  3.346113
    2    3.220090  3.606355
    3    3.794947  3.544400
    4    3.501432  3.534640
    5    3.490683  3.629012
    6    3.423810  3.213895
    7    3.794118  3.592581
'''


# pivot_table시에 어떤것을 index 로 하고 어떤것을 columns로 하는지에 대한 제약은 없지만 항목의 수가 많은 것을 column으로 두는것이 읽기가 쉬운것 같다.


r11 = df.pivot_table(values='rating',index='age',aggfunc='mean',columns='gender')
print (r11)


# 행열을 바꿔주는 함수 nustack()         => index를 columns 로 바꿔줌
r3 = r11.unstack()
print(r3)


















# print(df.head())
# '''
#    userid  movieid  rating  timestamp  ... gender age jop  zipcode
# 0       1     1193       5  978300760  ...      F   1  10    48067
# 1       1      661       3  978302109  ...      F   1  10    48067
# 2       1      914       3  978301968  ...      F   1  10    48067
# 3       1     3408       4  978300275  ...      F   1  10    48067
# 4       1     2355       5  978824291  ...      F   1  10    48067
# '''
#
# # 연습) 성별별로 별점의 평균을 알고싶다.
# # select gender, avg(rating) from df group by gender
# # record(줄) 이 2줄 나온다(남자, 여자 한줄씩)
# #  =>  pivot_table  :  ~별로
# # help(pd.DataFrame.pivot_table)
# # pivot_table(self, values=None, index=None, columns=None, aggfunc='mean',              fill_value=None, margins=False, dropna=True,
# #                                 => group by                => 함수(sum,max등) 적용       =>값이 None일땐 뭘로 채울까
#
# gender_mean = df.pivot_table(values='rating', index='gender')
# gender_mean2 = df.pivot_table(values='rating', index='gender',aggfunc='mean')
# gender_sum = df.pivot_table(values='rating', index='gender',aggfunc='sum')
# gender_min = df.pivot_table(values='rating', index='gender',aggfunc='min')
# gender_max = df.pivot_table(values='rating', index='gender',aggfunc='max')
# print(gender_mean)
# '''
#           rating
# gender
# F       3.620366
# M       3.568879
# '''
#
# print(gender_mean2)
# '''
# gender
# F       3.620366
# M       3.568879
# '''
#
# print(sum)
# '''
# gender
# F        892203
# M       2690110
#         rating
# '''
# print(max)
# '''
#         rating
# gender
# F            5
# M            5
# '''
# print(min)
# '''
#         rating
# gender
# F            1
# M            1
# '''
#
# # 나이별로 별점의 평균을 출력해 봅니다.
# # select age, avg(rating) from df group by age
# age_mean = df.pivot_table(values='rating',index='age',aggfunc='mean')
# print(age_mean)
# '''
# age
# 1    3.549520
# 18   3.507573
# 25   3.545235
# 35   3.618162
# 45   3.638062
# 50   3.714512
# 56   3.766632
# '''
#
# # 연습) 나이대별, 성별 별로 rating의 평균을 다음과같이 보여줘라
#
# # 컬럼(열)을 나누어 출력할 수 있다.
# age_mean_gender = df.pivot_table(values='rating', index='age',columns='gender',aggfunc='mean')
# # print(age_mean_gender)
# '''
# gender         F         M
# age
# 1       3.616291  3.517461
# 18      3.453145  3.525476
# 25      3.606700  3.526780
# 35      3.659653  3.604434
# 45      3.663044  3.627942
# 50      3.797110  3.687098
# 56      3.915534  3.720327
# '''
#
# # help(pd.DataFrame.pivot_table)
#
# # 컬럼과 인덱스를 바꿔서 출력
# gender_mean_age = df.pivot_table(values='rating', index='gender',columns='age',aggfunc='mean')
# print(gender_mean_age)
# '''
# age           1         18       25        35        45        50        56
# gender
# F       3.616291  3.453145  3.60670  3.659653  3.663044  3.797110  3.915534
# M       3.517461  3.525476  3.52678  3.604434  3.627942  3.687098  3.720327
# '''
# r = df.pivot_table(values='rating', index='age',columns='gender',aggfunc='mean')
#
# print(r)
# print(type(r))
# '''
# gender         F         M
# age
# 1       3.616291  3.517461
# 18      3.453145  3.525476
# 25      3.606700  3.526780
# 35      3.659653  3.604434
# 45      3.663044  3.627942
# 50      3.797110  3.687098
# 56      3.915534  3.720327
# '''
#
# r.index = ['under 18','18-24','25-34','35-44','45-49','50-55','56+']
# print(r)
# '''
# gender           F         M
# under 18  3.616291  3.517461
# 18-24     3.453145  3.525476
# 25-34     3.606700  3.526780
# 35-44     3.659653  3.604434
# 45-49     3.663044  3.627942
# 50-55     3.797110  3.687098
# 56+       3.915534  3.720327
# '''
# r.plot(kind='bar')
# plt.show()