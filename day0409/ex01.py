from sklearn import preprocessing
import numpy as np

# 때에 따라 존재하지 않은 임의의 특정값(feature)를 만들어야 하는 경우가 있을 수 있는데
# sklean의 preprossing을 이용하여 임의의 특징값을 생성해 봅시다
# add_dummy_feature     ===>       value를 생략하면 1을 각 행마다 추가해 준다.

x = [[0,1],[3,5]]
x2 = preprocessing.add_dummy_feature(x)
print(x2)
'''
[[1. 0. 1.]
 [1. 3. 5.]]
'''

x1 = [[0, 1, 2],[3, 4, 5]]

x3 = preprocessing.add_dummy_feature(x1,9)
print(x3)
'''
[[9. 0. 1. 2.]
 [9. 3. 4. 5.]]
'''

x4 = preprocessing.add_dummy_feature(x3,9)
print(x4)
'''
[[9. 9. 0. 1. 2.]
 [9. 9. 3. 4. 5.]]
'''