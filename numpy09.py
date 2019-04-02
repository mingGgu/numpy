import numpy as np

a = np.arange(12).reshape(-1,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(np.sum(a))
# 66 (전체 데이터 합을 구해줌)

print(np.sum(a, axis=0))
#[12 15 18 21]
# 열의 합이 나온다.

print(np.sum(a, axis=1))
# [ 6 22 38]
# 행의 합이 나온다.

print(np.max(a, axis=0))
# [ 8  9 10 11]
# 열중의 제일 큰 값

print(np.max(a, axis=1))
# [ 3  7 11]
# 행중의 제일 큰 값

b = np.zeros_like(a)
print(b)        #a배열과 동일한 shape의 배열을 생성하고 0으로 채워주세요
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

c = np.zeros(a.shape)
print(c)        #a배열과 동일한 shape의 배열을 생성하고 0으로 채워주세요
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

c = np.zeros(a.shape, dtype='int32')
print(c)        #a배열과 동일한 shape의 배열을 생성하고 0으로 채워주세요
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

# a = np.zeros([3,4], dtype='int32')
# print(a)
# # [[0 0 0 0]
# #  [0 0 0 0]
# #  [0 0 0 0]]





# a = np.zeros(3)
# print(a)
# # 3개의 배열을 0으로 채워줘 라는 뜻
#
# b = np.ones(10)
# print(b)