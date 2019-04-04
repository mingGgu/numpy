import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc, colors

#연습) score.csv파일을 읽어들여 학생의 이름을 index로 설정하고 이름 컬럼은 삭제합니다.
score = pd.read_csv('Data/scores.csv')
score.index=score['name']
del score['name']
print(score)
'''
        class  kor  eng  mat  bio
name                             
adam        1   67   87   90   98
andrew      1   45   45   56   98
ben         1   95   59   96   88
clark       1   65   94   89   98
dan         1   45   65   78   98
noel        1   78   76   98   89
paul        2   87   67   65   56
walter      2   89   98   78   78
oscar       2  100   78   56   65
martin      2   99   89   87   87
hugh        2   98   45   56   54
henry       2   65   89   87   78
'''

# 연습) 모든학생의 국어점수를 출력해 봅니다.
print(score.loc[ : ,'kor'])
print(score.iloc[:,1])
'''
name
adam       67
andrew     45
ben        95
clark      65
dan        45
noel       78
paul       87
walter     89
oscar     100
martin     99
hugh       98
henry      65
Name: kor, dtype: int64
'''

# 연습) 모든과목의 점수를 출력합니다.
subject = ['kor','eng','mat','bio']
print(score[subject])
print(score.loc[:,'kor':'bio'])
'''
        kor  eng  mat  bio
name                      
adam     67   87   90   98
andrew   45   45   56   98
ben      95   59   96   88
clark    65   94   89   98
dan      45   65   78   98
noel     78   76   98   89
paul     87   67   65   56
walter   89   98   78   78
oscar   100   78   56   65
martin   99   89   87   87
hugh     98   45   56   54
henry    65   89   87   78
'''

print(score.iloc[:,1:-1])
print(score.iloc[:,1:4])
'''
        kor  eng  mat
name                 
adam     67   87   90
andrew   45   45   56
ben      95   59   96
clark    65   94   89
dan      45   65   78
noel     78   76   98
paul     87   67   65
walter   89   98   78
oscar   100   78   56
martin   99   89   87
hugh     98   45   56
henry    65   89   87
'''

rc('font',family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf').get_name())

# 연습) ben학생의 과목별 점수를 막대그래프로 나타내 봅니다.

# ben = score.loc['ben','kor':'bio']
# print(len(ben))
x = ['kor','eng','mat','bio']

# plt.subplot(211)
# plt.bar(range(len(ben)),ben,0.4,color='g')
# plt.xticks(range(len(ben)), x,color='b')
# plt.title('ben 학생의 전과목 점수')
#
#
# # 연습) 모든학생의 국어점수를 막대그래프로 나타내 봅니다.
#
# student = score.loc[:,'kor']
# print(student)
#
# plt.subplot(212)
# plt.bar(range(len(student)),student,0.6,color=colors.TABLEAU_COLORS)
# x1 = student.index
# plt.xticks(range(len(student)),x1,color='b')
# plt.title('전체 학생의 국어점수')
# plt.show()



# # 연습) ben학생의 과목별 점수를 막대그래프로 나타내 봅니다.
# plt.bar(range(len(x)),score.loc['ben'][x],0.6,color='g')
# plt.title('ben의 과목별 점수')
# plt.xticks(range(len(x)),x)
# plt.show()
#
#
# # 연습) 모든학생의 국어점수를 막대그래프로 나타내 봅니다.
# plt.bar(range(len(score.index)), score['kor'])
# plt.xticks(range(len(score.index)),score.index,rotation=45)
# plt.title("학생별 국어점수")
# plt.show()

# 연습)두개의 차트를 파티션을 나누어 하나의 화면에 표시하세요

plt.subplot(211)

plt.bar(range(len(x)),score.loc['ben'][x],0.6,color='g')
plt.title('ben의 과목별 점수')
plt.xticks(range(len(x)),x)

plt.subplot(212)

plt.bar(range(len(score.index)), score['kor'])
plt.xticks(range(len(score.index)),score.index,rotation=45)
plt.title("학생별 국어점수")
a = plt.savefig('student.png')
print(a)
print('챠트를 만들었어요.')
# plt.show()