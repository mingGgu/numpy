import numpy as np

a = [0,1,2,3,4]
b = np.arange(5)

print(a)
print(type(a))
print(b)
print(type(b))

# a(리스트)를 numpy배열로 만들기
c = np.array(a)
print(c)
print(type(c))

# [0, 1, 2, 3, 4]
# <class 'list'>
# [0 1 2 3 4]
# <class 'numpy.ndarray'>
# [0 1 2 3 4]
# <class 'numpy.ndarray'>

d = [0,1,2,3,4,5]
arr = np.array(d)
print(arr)

arr2 = arr.reshape(2,3)
print(arr2)

print(arr.shape)
print(arr2.shape)

print(arr.ndim)
print(arr2.ndim)

print(arr.dtype)
print(arr2.dtype)

# [0 1 2 3 4 5]
# [[0 1 2]
#  [3 4 5]]
# (6,)
# (2, 3)
# 1
# 2
# int32
# int32

