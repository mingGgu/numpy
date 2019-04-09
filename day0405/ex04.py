# 연습) student01과 student02의 파일의 내용을 읽어들여
# 각각 df1과 df2에 담아봅니다

import numpy as np
import pandas as pd

df1 = pd.read_csv('../Data/student01',sep='::',engine='python')
# line terminator 는 engine이 c만 가능하다.

df2 = pd.read_csv('../Data/student02',sep='::',engine='python')
# print(df1)
# print(df2)

df = pd.merge(df1,df2)
print(df)
'''
      name  kor  eng  mat  bio  class  age
0     adam   67   87   90   98      1   27
1   andrew   45   45   56   98      1   25
2      ben   95   59   96   88      1   25
3    clark   65   94   89   98      1   25
4      dan   45   65   78   98      1   45
5     noel   78   76   98   89      1   28
6     paul   87   67   65   56      2   27
7   walter   89   98   78   78      2   29
8    oscar  100   78   56   65      2   20
9   martin   99   89   87   87      2   29
10    hugh   98   45   56   54      2   28
11   henry   65   89   87   78      2   25
'''

