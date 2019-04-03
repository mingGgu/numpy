import numpy as np

# size  =>  배열의 요소의 수를 알 수있다
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(a.size)

print(a)
'''
[[1 2 3]
 [4 5 6]]
'''

print(b)
'''
[1 2 3 4 5 6]
'''

print(a.size)
'''
6
'''

#2차원에서 1차원배열로 차원을 바꿀때 알아서 해줘! 하는것이 -1
c = a.reshape(-1)
print(c)
'''
[1 2 3 4 5 6]
'''

# # numpy배열의 차원을 변경       => reshape
# a = np.array([1,2,3,4,5,6])
# b = a.reshape([2,3])
#
# print(a)
# '''
# [1 2 3 4 5 6]
# '''
#
# print(b)
# '''
# [[1 2 3]
#  [4 5 6]]
# '''
#
# # 차원을 변경할때 행이나 열중에 하나를 생략       => -1
# c = np.array([1,2,3,4,5,6])
# d = c.reshape([-1,3])
#
# print(c)
# '''
# [1 2 3 4 5 6]
# '''
#
# print(d)
# '''
# [[1 2 3]
#  [4 5 6]]
# '''
# # 2차원배열을 1차원 배열로 만들때는 내가 직접 데이터의 수를 파악하기보다는 shape을 통해 행 * 열 만큼의 배열을 생성하도록 합니다.
# e = np.array([[1,2,3],[4,5,6]])
# f = e.reshape(len(e) * len(e[0]))
# print(e)
# print(f)
# '''
# e = [[1 2 3]
#     [4 5 6]]
#
# f = [1 2 3 4 5 6]
# '''
#
# row, col = e.shape
# g = e.reshape(row * col)
# print(g)
# '''
# g = [1 2 3 4 5 6]
# '''
# a = np.array([1,2,3,4,5])
# b = np.array([10.5,2.7,3.5])
# c = np.array([[1,2,3],[4,5,6]])
#
# print(a)
# print(b)
# '''
# a = [1 2 3 4 5]
# b = [10.5  2.7  3.5]
# '''
#
# # 배열의 자료형 type ==> 배열자체가 numpy배열인지 python배열인지
# print(type(a))
# print(type(b))
# '''
# <class 'numpy.ndarray'>
# <class 'numpy.ndarray'>
# '''
#
# # 배열의 요소의 자료형
# print(a.dtype)
# print(b.dtype)
# '''
# int32
# float64
# '''
#
# # 배열의 차수         =>ndim
# # 모양(몇행 몇열인지) => shape
# # 요소의 자료형       => dtype
#
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# '''
# a = 1
# b = 1
# c = 2
# '''
#
# print(a.shape)
# print(b.shape)
# print(c.shape)
# '''
# a = (5,)
# b = (3,)
# c = (2, 3)
# '''
#

# a = np.arange(10,-10,-1)
# b = list(a)
# print(a)
# print(b)
# '''
# a = [10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9]
# b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# '''
# print(type(a))
# print(type(b))
# '''
# a = <class 'numpy.ndarray'>
# b = <class 'list'>
# '''
# 파이썬배열 => numpy배열              np.array
# numpy배열 => 파이썬배열              list
#
# a = [1,2,3,4,5]
# na = np.array(a)
# print(a)
# print(na)
# '''
# [1, 2, 3, 4, 5] // list(파이썬배열)
# [1 2 3 4 5]     // array(numpy배열)
# '''
# print(a[2])
# print(na[2])
# # 둘다 3이라는 값을 출력한다.

# 연속 된 데이터를 갖는 numpy 배열 생성
# np.arange
# a = np.arange(10)
# print(a)
# '''
# [0 1 2 3 4 5 6 7 8 9]
# '''
#
# b = np.arange(1,11)
# print(b)
# '''
# [ 1  2  3  4  5  6  7  8  9 10]
# '''
#
# c = np.arange(1,11,2)
# print(c)
# '''
# [1 3 5 7 9]
# '''
#
# d = np.arange(10,-10,-1)
# print(d)
# '''
# [10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3 -4 -5 -6 -7 -8 -9]
# '''

# a = np.zeros(10, dtype='int32')
# b = np.ones(5,dtype='int32')
# c = np.full(7,20)
#
# print(a)
# print(b)
# print(c)

# a = np.zeros([2,3], dtype='int32')
# print(a)
# print('-'*20)
# b = np.ones([5,5], dtype='int32')
# print(b)
# print('-'*20)
# c = np.full([5,5],100, dtype='int32')
# print(c)


