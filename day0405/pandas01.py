import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc, colors

# Data 앞의 / 는 루트로 부터 라는 뜻이고
# 루트는 numpytest 최상의 폴더를 말함
# data = pd.read_csv('/Data/socres.csv')
data = pd.read_csv('../Data/scores.csv')
# print(data)
'''
    class    name  kor  eng  mat  bio
0       1    adam   67   87   90   98
1       1  andrew   45   45   56   98
2       1     ben   95   59   96   88
3       1   clark   65   94   89   98
4       1     dan   45   65   78   98
5       1    noel   78   76   98   89
6       2    paul   87   67   65   56
7       2  walter   89   98   78   78
8       2   oscar  100   78   56   65
9       2  martin   99   89   87   87
10      2    hugh   98   45   56   54
11      2   henry   65   89   87   78
'''

# 학생들 중에 1반학생만 뽑아 오고 싶다.
# pandas의 DataFrame에 추출할 행에 조건식을 부여할 수 있다.

# dataframe으로부터 class 컬럼의 속성이 1인지 판별하여 boolean Array를 얻어보자
arr_1 = data['class'] == 1
print(arr_1)
'''
0      True
1      True
2      True
3      True
4      True
5      True
6     False
7     False
8     False
9     False
10    False
11    False
Name: class, dtype: bool
'''

class1 = data[arr_1]
print(class1)
'''
# 값이 True인 애들만 뽑아오기때문에 1반애들만 추출한다.

   class    name  kor  eng  mat  bio
0      1    adam   67   87   90   98
1      1  andrew   45   45   56   98
2      1     ben   95   59   96   88
3      1   clark   65   94   89   98
4      1     dan   45   65   78   98
5      1    noel   78   76   98   89
'''

# 연습)1반학생의 과목별 평균을 출력

# 1반 학생만 뽑기
class_1 = data[data['class'] == 1]

# class를 없애기
del class_1['class']
# index를 name으로 바꾸기
class_1.index = class_1['name']
# 컬럼에있는 name을 없애기
del class_1['name']
print(class_1)
'''
name                      
adam     67   87   90   98
andrew   45   45   56   98
ben      95   59   96   88
clark    65   94   89   98
dan      45   65   78   98
noel     78   76   98   89
'''

print(class_1.mean())
'''
kor    65.833333
eng    71.000000
mat    84.500000
bio    94.833333
'''

print(class_1.mean(axis=1))
'''
# 학생별 평균(행으로 평균을 내주세요-> axis=1)
name
adam      85.50
andrew    61.00
ben       84.50
clark     86.50
dan       71.50
noel      85.25
'''

sumkor = sum(class1['kor'])
sumeng = sum(class1['eng'])
summat = sum(class1['mat'])
sumbio = sum(class1['bio'])

a = len(class1['name'])
kkk = sumkor / a

avgKor = np.average(class1['kor'])
avgEng = np.average(class1['eng'])
avgMat = np.average(class1['mat'])
avgBio = np.average(class1['bio'])

# 연습)1반학생들의 성적을 막대그래프로 나타내 봅니다.

# rc('font', family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf').get_name())
# plt.bar(range(len(class_1.index)), class_1['kor'], 0.6, color='pink')
# plt.title('1반학생의 과목별 점수')
# plt.xticks(range(len(class_1.index)), class_1.index)
# plt.show()
#
# class_1.plot()
class_1.plot(kind='hexbin')
plt.show()

# help(pd.DataFrame.plot)
