import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

sty = plt.style.available
# ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale',
#  'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
#  'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
#  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
#  'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']

data1 = np.random.randint(-1,2,100)
data2 = np.cumsum(data1)

print(len(sty)-1)
for a in range(len(sty)-1):
    with plt.style.context(sty[a]):
        # 5행 5열
        plt.subplot(5,5,a+1)
        plt.title(sty[a])
        plt.plot(data2)
plt.show()

sty = plt.style.available
sty = sty[:-1]

data1 = np.random.randint(-1,2,100)
data2 = np.cumsum(data1)

i = 1

for a in sty:
    with plt.style.context(a):
        # 5행 5열
        plt.subplot(5,5,i)
        plt.title(a)
        plt.plot(data2)
    i = i + 1
plt.show()




# 누적 더 간단하게 해보기
# data1 = np.random.randint(-1,2,100)
# print(data1)
# # 누적된 합을 만들어주는 함수
# data2 = np.cumsum(data1)
# print(data2)
#
# plt.subplot(2,1,1)
# plt.plot(data1)
# plt.subplot(2,1,2)
# plt.plot(data2)
# plt.show()









# # 0과 100사이의 난수 1개 만들어줘
# x = np.random.randint(100)
# print(x)
#
# # 0에서 1000사이의 난수를 100개 만들어줘
# x1 = np.random.randint(0,1000,100)
# print(x1)
#
# lotto = np.random.randint(1,45,6)
# print(lotto)
# '''
# [ 3 18 31 41 12 17]
# [14 20 31 31  5  9]
# [18 44 39 12 42 14]
# [11 19 16 25 33 26]
# [34 27  9  5 43 26]
# '''
#
# # 0~1사이의 실수 1개 발생
# x2 = np.random.rand()
# print(x2)
#
# # 0~100사이의 정수 1개 만들기
# x3 = np.random.randint(100)
# print(x3)
#
# # 0~1사이의 실수 100개 만들기
# x4 = np.random.rand(100)
# print(x4)
# y = np.random.rand(100)
#
# # 데이터의 흩어진 정도를 점을찍어 파악하고자 할 때 ==> scatter (분포도 파악)
# plt.plot(x4,y,c='r')
# plt.show()
#

# 연습)x, y배열을 만들고 x에는 난수 100개를 발생시켜 담도록 합니다. (단, 난수의 범위는 -1,0,1 중 하나가 되도록)
# y에는 x의 요소를 누적한 합이 담기도록 합니다.
# x와 y를 각각 하나의 figure에 위아래로 분할하여 plot으로 나타내 봅니다.

# x = np.random.randint(-1,2,100)
# data1 = x
#
# y = 0
# data2 = []
# for i in x:
#     y = y + i
#     data2.append(y)
# print(data1)
# print(data2)
#
# plt.subplot(211)
# plt.plot(data1)
# plt.subplot(212)
# plt.plot(data2)
# plt.show()

# data1 = []
# data2 = []
# temp = 0
# for _ in range(100):
#     # 그냥 3 일땐 0,1,2 인데 여기에 -1 하면 -1,0,1 이된다.
#     a = np.random.randint(3)-1
#     temp = temp + a
#     data1.append(a)
#     data2.append(temp)
# # print(data1)
# # print(data2)
#
# plt.subplot(211)
# plt.plot(data1)
# plt.subplot(212)
# plt.plot(data2)
# plt.show()
#
#

# # 이미 있는 데이터들 중에 임의로 하나를 선택하고 싶다.         random => choice
# data = [9,7,2,1,100,3]
#
# # 데이터들 중 하나를 선택
# x = random.choice(data)
# print(x)
#
# # 이미 있는 데이터들 중에 중복없이 임의로 여러개 뽑고싶다.     random => sample
# x1 = random.sample(data, 3)
# print(x1)
# '''
# [1, 3, 2]
# '''
# # random와 numpy를 이용할 수있다.
#
# # 0~10사이의 난수를 발생해줘
# x = np.random.randint(10)
# print(x)
#
# # 시작값을 줘야함.
# x1 = random.randint(0,10)
# print(x1)
#
# # 100에서 1000사이의 난수 5개 만들어줘
# x2 = np.random.randint(100,1000,5)
# print(x2)
#
# # 0에서 1000사이에 난수 하나 만들어줘
# x3 = np.random.randint(1000)
# print(x3)














