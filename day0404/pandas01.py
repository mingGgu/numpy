# numpy         배열의 조작을 편리하게 해준다.
# pandas        데이터프레임의 조작을 편리하게 해준다.

# 또 머신러닝을 위한 많은 라이브러리들이 상대하는 데이터형태가 numpy 이거나 pandas를 취급한다.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = pd.Series([['박민서','김경희','이혜민'],['박민서','김경희','이혜민']])
print(arr)
'''
0    [박민서, 김경희, 이혜민]
1    [박민서, 김경희, 이혜민]
dtype: object
'''


# arr = pd.Series([[1,2,3],[4,5,6]])
# print(arr)
# '''
# 0    [1, 2, 3]
# 1    [4, 5, 6]
# dtype: object
# '''
#
# print(arr[0])
# '''
# [1, 2, 3]
# '''
#
# print(type(arr[0]))
# '''
# <class 'list'>
# '''
#
# print(arr[0][1])
# '''
# 2
# '''










# arr = pd.Series(['박민서','김경희','이혜민','이필숙','도경수'])
# print(arr)
# '''
# 0    박민서
# 1    김경희
# 2    이혜민
# 3    이필숙
# 4    도경수
# dtype: object
# '''
#
# name = list(arr)
# print(name)
# '''
# ['박민서', '김경희', '이혜민', '이필숙', '도경수']
# '''
#
# print(type(arr))
# print(type(name))
# '''
# <class 'pandas.core.series.Series'>
# <class 'list'>
# a = [1,2,3,4,5]
# arr = pd.Series(a)
# print(arr)
# '''
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# '''
#
# print(a)
# '''
# [1, 2, 3, 4, 5]
# '''
#
# print(type(a))
# print(type(arr))
# '''
# <class 'list'>
# <class 'pandas.core.series.Series'>
# '''
#
