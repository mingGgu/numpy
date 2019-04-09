import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 연습) 수학점수가 평균이하인 모든 학생의 성적을 막대그래프로 나타내 봅니다.

rc('font', family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf').get_name())
score = pd.read_csv('../Data/scores.csv')
score.index = score['name']
del score['name']

# 수학점수의 평균을 계산
mean_math = score['mat'].mean()
print(mean_math)
'''
78.0
'''

# 학생들 중 수학점수가 평균(78점)이하인 학생들의 정보를 추출
lower_mean = score[score['mat'] <= mean_math]
print(lower_mean)
'''
        class  kor  eng  mat  bio
name                             
andrew      1   45   45   56   98
dan         1   45   65   78   98
paul        2   87   67   65   56
walter      2   89   98   78   78
oscar       2  100   78   56   65
hugh        2   98   45   56   54
'''

lower_mean[['kor','eng','mat','bio']].plot(kind='bar',colormap='winter_r')
plt.show()



# 데이터가 너무 많을때 head를 이용하여 몇개만 뽑자
print(score.head())
'''
        class  kor  eng  mat  bio
name                             
adam        1   67   87   90   98
andrew      1   45   45   56   98
ben         1   95   59   96   88
clark       1   65   94   89   98
dan         1   45   65   78   98
'''

# head로 5개만 추출했는데도 정신이 없을수 있다.
# 이때는 데이터 하나만 뽑아와서 데이터의 성격을 파악하고 싶다.
print(score.head(1))
'''
      class  kor  eng  mat  bio
name                           
adam      1   67   87   90   98
'''





# rc('font', family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf').get_name())
# score = pd.read_csv('../Data/scores.csv')
# score.index = score['name']
# del score['name']
# print(score)
#
# matAvg = score['mat'].mean()
# print(matAvg)
# '''
# 78.0
# '''
#
# score_mat = score['mat'] <= matAvg
# matscore = score[score_mat]
# print(matscore)
# '''
#         class  kor  eng  mat  bio
# name
# andrew      1   45   45   56   98
# dan         1   45   65   78   98
# paul        2   87   67   65   56
# walter      2   89   98   78   78
# oscar       2  100   78   56   65
# hugh        2   98   45   56   54
# '''
#
# matavg_mat = matscore['mat']
# plt.title('수학 평균 이하의 점수인 학생')
# matavg_mat.plot(kind='bar')
# print(plt.colormaps())
# plt.show()


