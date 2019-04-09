import ex02
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = ex02.getMovie()

# 나이대별, 설별 별점의 평균

mean = df.pivot_table(values='rating', index='age',columns='gender', aggfunc='mean')
sum = df.pivot_table(values='rating', index='age',columns='gender', aggfunc='sum')
print(mean)
print(sum)

# 두가지를 병합하고싶다.

# r3 = pd.merge(mean,sum)
# print(r3)
# 오류남 : mean과 sum의 성질이 달라서 병합할 수 없다.

r3 = pd.concat([mean,sum])
print(r3)
'''
gender              F             M
age                                
1            3.616291  3.517461e+00
18           3.453145  3.525476e+00
25           3.606700  3.526780e+00
35           3.659653  3.604434e+00
45           3.663044  3.627942e+00
50           3.797110  3.687098e+00
56           3.915534  3.720327e+00
1        31921.000000  6.466500e+04
18      156866.000000  4.869000e+05
25      329436.000000  1.072903e+06
35      181054.000000  5.389710e+05
45       88316.000000  2.159460e+05
50       68591.000000  2.006740e+05
56       36019.000000  1.100510e+05
'''

r4 = pd.concat([mean,sum],axis=1)
print(r4)
'''
gender         F         M       F        M
age                                        
1       3.616291  3.517461   31921    64665
18      3.453145  3.525476  156866   486900
25      3.606700  3.526780  329436  1072903
35      3.659653  3.604434  181054   538971
45      3.663044  3.627942   88316   215946
50      3.797110  3.687098   68591   200674
56      3.915534  3.720327   36019   110051
'''









# # help(pd.DataFrame.pivot_table)
# # 연습) 나이대별, 성별별로 별점의 평균과 합을 출력해 봅시다.
# # 혹시 오류가 나면 그것을 해결해 봅시다.
#
# avg_sum = df.pivot_table(values='rating', index='age',columns='gender', aggfunc=['mean','sum'])
# print(avg_sum)
#
# avg_sum1 = df.pivot_table(values='rating', index='age',columns='gender', aggfunc=[np.mean,np.sum])
# print(avg_sum1)
# '''
#             mean               sum
# gender         F         M       F        M
# age
# 1       3.616291  3.517461   31921    64665
# 18      3.453145  3.525476  156866   486900
# 25      3.606700  3.526780  329436  1072903
# 35      3.659653  3.604434  181054   538971
# 45      3.663044  3.627942   88316   215946
# 50      3.797110  3.687098   68591   200674
# 56      3.915534  3.720327   36019   110051
# '''
# # r1 = df.pivot_table(values='rating',index='gender',aggfunc='mean')
# # print(r1)
# #
# # r2 = r1.unstack()
# # print(r2)
# '''
#
#           rating
# gender
# F       3.620366
# M       3.568879
#
#         gender
# rating  F         3.620366
#         M         3.568879
# dtype: float64
# '''
#
# r1 = df.pivot_table(values='rating',index=['gender','age'],aggfunc='mean')
# print(r1)
#
# r2 = r1.unstack()
# print(r2)
# '''
#               rating
# gender age
# F      1    3.616291
#        18   3.453145
#        25   3.606700
#        35   3.659653
#        45   3.663044
#        50   3.797110
#        56   3.915534
# M      1    3.517461
#        18   3.525476
#        25   3.526780
#        35   3.604434
#        45   3.627942
#        50   3.687098
#        56   3.720327
#
#           rating
# age           1         18       25        35        45        50        56
# gender
# F       3.616291  3.453145  3.60670  3.659653  3.663044  3.797110  3.915534
# M       3.517461  3.525476  3.52678  3.604434  3.627942  3.687098  3.720327
# '''
#
# r3 = r2.stack()
# print(r3)
#
