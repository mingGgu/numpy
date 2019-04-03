import numpy as np

# 연습) 속은 0으로 채워지고 테두리는 1로 채워지는 5*5 배열 만들기

a = np.ones([5,5],dtype='int32')
print(a)
a[1:4,1:4] = 0
a[1:-1,1:-1] = 0 #같은말 (1:-1 이런 표현에서는 라스트인덱스를 포함하지 않는다.)
print('ones로 채운뒤')
print(a)

b = np.zeros([5,5],dtype='int32')
print('zeros로 채운뒤1')
rows =[0,0,0,0,0,4,4,4,4,4,1,2,3,1,2,3]
cols = [0,1,2,3,4,0,1,2,3,4,0,0,0,4,4,4]
b[rows,cols] = 1
print(b)

c = np.zeros([5,5],dtype='int32')
c[0 -1,:] = 1
'''
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [1 1 1 1 1]]
'''

c[[0, -1],:] = 1
'''
[[1 1 1 1 1]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [1 1 1 1 1]]
#  index array [0, -1] 의 뜻은 처음과 마지막 행,열 을 뜻한다.
    행 자리에 [0, -1]을 넣어줬기때문에 여기서는 처음과 마지막 행을 뜻한다.
    즉, 위의 fancy array의 뜻은 모든 열에 대하여 처음과 마지막 행을 1로 채워주세요 라는 말
'''
c[:,[0,-1]] = 1
'''
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
'''
print(c)

# 대각선 만들기
# rows =[0,1,2,3,4]
# cols = [0,1,2,3,4]