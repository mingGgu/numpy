import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a = pd.Series([5,9,3,7])
# print(a)
# '''
# 0    5
# 1    9
# 2    3
# 3    7
# dtype: int64
# '''
#
# print(a.values)
# print(type(a.values))
# '''
# [5 9 3 7]
# <class 'numpy.ndarray'>
# '''

# Pandas의 Series는 자바의 map과 같이 key value가 한쌍으로 이루어지는 자료구조를 표현하기에 적합하다.
# key를 부여하지 않으면 차례대로 index가 부여된다. 필요하다면 key를 부여할 수 있다.


# pandas의 Series는 파이썬 배열을 갖고 key값을 부여해 보다 직관적으로 접근할 수 있다.
# 그렇다면 파이썬 딕셔너리를 갖고도 Series를 만들 수 있는지 실험

a = {'박민서':5,'김경희':9,'이혜민':3,'이필숙':10,'도경수':12}
print(a)
print(type(a))
'''
{'박민서': 5, '김경희': 9, '이혜민': 3, '이필숙': 10, '도경수': 12}
<class 'dict'>
'''
s = pd.Series(a)
print(s)
'''
박민서     5
김경희     9
이혜민     3
이필숙    10
도경수    12
dtype: int64
'''






#
# keys = a.index              #Series의 key값으로 모두 뽑아온다.
# for key in keys:           #key의 개수만큼 반복수행하여 각요소의 key의 value를 출력
#     print(key, a[key])
#     '''
#     박민서 5
#     김경희 9
#     이혜민 3
#     이필숙 7
#     도경수 6
#     '''

# print(a)
# '''
# 박민서    5
# 김경희    9
# 이혜민    3
# 이필숙    7
# 도경수    6
# dtype: int64
# '''
#
# print(a['이혜민'])
# print(a[2])
# '''
# 3
# 3
# '''
# print(a[0])
# print(a[-1])
# '''
# 5
# 6
# '''
# print(a.index)
# '''
# Index(['박민서', '김경희', '이혜민', '이필숙', '도경수'], dtype='object')
# '''