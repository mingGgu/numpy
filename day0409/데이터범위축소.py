from sklearn import preprocessing
import numpy as np

# 때에따라 데이터의 범위를 축소시켜야 할 때가 있다.
# 값의 범위가 큰 것보다는 값의 범위가 작은것이
# 기계학습에 효율을 높일 수 있다.
# 가급적 문자데이터 보다는 숫자 데이터를 훈련 시키는 것이 더 좋고
# 가급적 숫자의 범위를 이진화 시키는 것이 기계학습에 훨씬 효율성 높다.

x = [[1,-1,3],[2,0,0],[0,1,-1]]

# 2진화 시켜줌
binarizer = preprocessing.Binarizer()
print(binarizer)
print(type(binarizer))
'''
Binarizer(copy=True, threshold=0.0)
<class 'sklearn.preprocessing.data.Binarizer'>
'''
r = binarizer.fit(x)
b = r.transform(x)
print(b)
'''
[[1 0 1]
 [1 0 0]
 [0 1 0]]
'''
b1 = preprocessing.Binarizer().fit(x).transform(x)
print(b1)
'''
[[1 0 1]
 [1 0 0]
 [0 1 0]]
'''
