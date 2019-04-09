import numpy as np
import pandas as pd

scores = pd.read_csv('../Data/scores.csv')
print(scores)
# 각학생별 평균을 구하여 출력


print(scores.mean())
# 과목별로 평균구해짐
'''
class     1.500000
kor      77.750000
eng      74.333333
mat      78.000000
bio      82.250000
dtype: float64
'''

print(scores.mean(axis=1))
#axis=1을 넣어주면 행평균 구해짐. 여기서는 class까지 더해져서 평균 구해진것
'''
0     68.6
1     49.0
2     67.8
3     69.4
4     57.4
5     68.4
6     55.4
7     69.0
8     60.2
9     72.8
10    51.0
11    64.2
'''
print(scores[['kor','eng','mat','bio']].mean(axis=1))
# class빼고 과목만 포함해 평균구함.
'''
0     85.50
1     61.00
2     84.50
3     86.50
4     71.50
5     85.25
6     68.75
7     85.75
8     74.75
9     90.50
10    63.25
11    79.75
dtype: float64
'''


# 구해진 각 학생별의 평균을 avg라는 속성으로 추가해준다.
scores['avg'] = scores[['kor','eng','mat','bio']].mean(axis=1)
# print(scores)
'''
 class    name  kor  eng  mat  bio    avg
0       1    adam   67   87   90   98  85.50
1       1  andrew   45   45   56   98  61.00
2       1     ben   95   59   96   88  84.50
3       1   clark   65   94   89   98  86.50
4       1     dan   45   65   78   98  71.50
5       1    noel   78   76   98   89  85.25
6       2    paul   87   67   65   56  68.75
7       2  walter   89   98   78   78  85.75
8       2   oscar  100   78   56   65  74.75
9       2  martin   99   89   87   87  90.50
10      2    hugh   98   45   56   54  63.25
11      2   henry   65   89   87   78  79.75
'''