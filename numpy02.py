import numpy as np

a =[1,2,3,4,5]
b =[1.0,2.0,3.0,4.0,5.0]
c = ['a','b','c','d','e']
d = ['hello','java','python','oracle','mongo','우리나라','대한민국대한민국대한민국대한민국대한민국']

e = ['박민서','도경수','김경희','이혜민','디오']

arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)
arr4 = np.array(d)
arr5 = np.array(e)

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)

# int32
# float64
# <U1  u = unicode이며, 숫자는 사용된 글자크기 ? 라고 할 수 있다.
# <U20
# <U3

print(arr1.dtype)
print(arr1.shape)
print(arr1.ndim)

# int32     안에 들어간 데이터의 자료형이 정수형이다.
# (5,)      1차원이면서 데이터의 수가 5개이다
# 1         1차원이다









