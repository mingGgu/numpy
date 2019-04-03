import numpy as np

# broadCasting 에 비교연산자를 사용하면 boolean Array를 반환한다.
a = np.array([1,3,0,7,9,5,6])
b = a > 5
print(b)
'''
[False False False  True  True False  True]
'''

# 배열의 요소중에 원하는 인덱스의 요소만 추출할 수 있다   =>  indexArray
c = np.array([1,3,0,7,9,5,6])
print(c[[0,2,5]])
'''
[1 0 5]
'''

# -- 여러개의 인덱스 요소를 한번에 출력 하고자 할때 2차원 배열로 정의하는 이유 --
# 1차원, c[0,2,5] 로 출력하면 3차원 배열로 인식해 0번째 행의 2번째 열, 5번째 면에 해당하는 값을 가져오려고 한다.
print(c[0])
'''
1
'''

# 0,2,5 요소만 출력하는 것을 boolean Array로 실험 해 봅니다.
r = [True, False, True,  False,  False, True,  False]
print(a[r])
'''
[1 0 5]
'''


# #numpy 배열의 연산
# # Broad Casting         =>  어떤 값 하나가 배열의 요소만큼 연산을 수행하는 것
# # Vector Operation      =>  두개의 배열의 인덱스가 같은 요소끼리 연산을 수행
# #                           열의 크기가 같아야한다.
#
# a = np.array([1,2,3,4,5])
# b = a + 1
# print(b)
# '''
# [2 3 4 5 6]     # 배열의 요소에 각각 1을 더해줍니다. Broad Casting
# '''
#
# c = np.array([1,2,3])
# d = np.array([4,5,6])
# e = c + d
# print(e)
# '''
# [5 7 9]         # Vector Operation
# '''
#
# f = np.array([[1,2,3],[4,5,6]])
# g = np.array([[10,20,30],[40,50,60]])
# # f,g 두배열을 더해봅니다.
# # [[11,22,33],[44,55,66]]
# print(f+g)
# '''
# [[11 22 33]
#  [44 55 66]]
# '''
#
# h = np.array([1,2,3,4,5,6])
# i = np.array([[10,20,30],[40,50,60]])
# # h,i 두배열을 더해봅니다.
# # [[11,22,33],[44,55,66]]
# h1 = h.reshape([2,-1])
# # h1 = h.reshape([2,3])
# print(h1 + i)
# '''
# [[11 22 33]
#  [44 55 66]]
# '''






























