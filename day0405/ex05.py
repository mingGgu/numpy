# 병합하고자하는 두개의 파일의 데이터 수가 일치하지 않았을 때
# dan학생의 점수정보는 없다.

import numpy as np
import pandas as pd

df1 = pd.read_csv('../Data/stu01',sep='::',engine='python')
df2 = pd.read_csv('../Data/stu02',sep='::',engine='python')
print(df1)
'''
      name  kor  eng  mat  bio
0     adam   67   87   90   98
1   andrew   45   45   56   98
2      ben   95   59   96   88
3    clark   65   94   89   98
4     noel   78   76   98   89
5     paul   87   67   65   56
6   walter   89   98   78   78
7    oscar  100   78   56   65
8   martin   99   89   87   87
9     hugh   98   45   56   54
10   henry   65   89   87   78
'''
print(df2)
'''
    class    name  age
0       1    adam   27
1       1  andrew   25
2       1     ben   25
3       1   clark   25
4       1     dan   45
5       1    noel   28
6       2    paul   27
7       2  walter   29
8       2   oscar   20
9       2  martin   29
10      2    hugh   28
11      2   henry   25
'''
df = pd.merge(df1,df2)
print(df)
'''
      name  kor  eng  mat  bio  class  age
0     adam   67   87   90   98      1   27
1   andrew   45   45   56   98      1   25
2      ben   95   59   96   88      1   25
3    clark   65   94   89   98      1   25
4     noel   78   76   98   89      1   28
5     paul   87   67   65   56      2   27
6   walter   89   98   78   78      2   29
7    oscar  100   78   56   65      2   20
8   martin   99   89   87   87      2   29
9     hugh   98   45   56   54      2   28
10   henry   65   89   87   78      2   25
'''
# 일치하는 것 만 나옴


# 실습) 서로 일치하지 않는 데이터 dan의 정보도 나타내 봅니다. dan학생의 정보는 0으로 출력합니다.
# help(pd.merge)
'''
    how : {'left', 'right', 'outer', 'inner'}, default 'inner'
        Type of merge to be performed.
    
        * left: use only keys from left frame, similar to a SQL left outer join;
          preserve key order.
        * right: use only keys from right frame, similar to a SQL right outer join;
          preserve key order.
        * outer: use union of keys from both frames, similar to a SQL full outer
          join; sort keys lexicographically.
        * inner: use intersection of keys from both frames, similar to a SQL inner
          join; preserve the order of the left keys.
'''

# outer join하면 될듯
df = pd.merge(df1,df2,how='outer')
# 결측치를 0으로 채워줘
df.fillna(0,inplace=True)
print(df)
'''
      name    kor   eng   mat   bio  class  age
0     adam   67.0  87.0  90.0  98.0      1   27
1   andrew   45.0  45.0  56.0  98.0      1   25
2      ben   95.0  59.0  96.0  88.0      1   25
3    clark   65.0  94.0  89.0  98.0      1   25
4     noel   78.0  76.0  98.0  89.0      1   28
5     paul   87.0  67.0  65.0  56.0      2   27
6   walter   89.0  98.0  78.0  78.0      2   29
7    oscar  100.0  78.0  56.0  65.0      2   20
8   martin   99.0  89.0  87.0  87.0      2   29
9     hugh   98.0  45.0  56.0  54.0      2   28
10   henry   65.0  89.0  87.0  78.0      2   25
11     dan    0.0   0.0   0.0   0.0      1   45
'''
