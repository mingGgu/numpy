import numpy as np

a = np.arange(3)
b = np.arange(6)
c = np.arange(3).reshape(-1,3)      #2차원 배열로 만들어줌
d = np.arange(6).reshape(-1,3)
e = np.arange(3).reshape(3,-1)

# print('a+b:', a+b)      #오류남 :ValueError: operands could not be broadcast together with shapes (3,) (6,)
print('a+c:', a+c)       #[[0 2 4]]
# [0 1 2]+[[0 1 2]]
print('a+d:', a+d)       #[[0 2 4]
                          #[3 5 7]]
# [0 1 2]+[[0 1 2]
#         [3 4 5]]

print('a+e:', a+d)       #[[0 2 4]          vector operation과 broad casting도 수행했음
                          # [3 5 7]]        a의 1행이 d의 1행과 한번, 2go
# [0 1 2]+[[0]
#          [1]
#          [2]]

# print('b+c',b+c)        #오류남 :ValueError: operands could not be broadcast together with shapes (6,) (1,3)
# print('b+d',b+d)        #오류남 :ValueError: operands could not be broadcast together with shapes (6,) (2,3)

print('b+e',b+e)         #[[0 1 2 3 4 5]
                          # [1 2 3 4 5 6]
                          # [2 3 4 5 6 7]]
# [0 1 2 3 4 5]+[[0]
#                [1]
#                [2]]
print('c+d',c+d)         # [[0 2 4]
                          # [3 5 7]]
# [[0 1 2]]+[[0 1 2]
#           [3 4 5]]
print('c+e',c+e)         #[[0 1 2]
                          #[1 2 3]
                          #[2 3 4]]
# [[0 1 2]]+[[0]
#            [1]
#            [2]]
# print('d+e',d+e)        #오류남 :ValueError: operands could not be broadcast together with shapes (2,3) (3,1)

print(a)
print(b)
print(c)
print(d)
print(e)