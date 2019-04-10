import numpy as np
import pandas as pd

age = [28,20,28,29]
addr = ['서울','마산','서울','대전','광주']

b_age = pd.get_dummies(age)
print(b_age)
'''
   20  28  29
0   0   1   0   :   28
1   1   0   0   :   20
2   0   1   0   :   28
3   0   0   1   :   29
'''

b_addr = pd.get_dummies(addr)
print(b_addr)
'''
   광주  대전  마산  서울
0   0     0    0     1
1   0     0    1     0
2   0     0    0     1
3   0     1    0     0
4   1     0    0     0
'''
