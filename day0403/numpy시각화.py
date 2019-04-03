import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

path = 'C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf'
fontprop = fm.FontProperties(fname=path, size=18)

qty = [10,20,10,30,50]
# bar가 몇개인지, 어떤걸 나타낼건지,막대그래프 굵기
plt.bar(range(len(qty)),qty,0.4)
plt.title('요일별 과일 판매량',fontproperties=fontprop)
plt.show()






# print(np.exp(2))
# print(np.log(2))
# '''
# 7.38905609893065
# 0.6931471805599453
# '''
#
# # 연습) 0.01에서 0.01씩 증가하여 2까지의 수들에 대한 지수값과 로그값을 하나의 화면에 차트를 그려보세요
# # 두개의 차트를 가로로 나타내 봅니다.
#
# z = np.arange(0.01,2,0.01)
# a = np.exp(z)
# b = np.log(z)
# plt.subplot(121)
# plt.plot(a,'ro')
# plt.subplot(122)
# plt.plot(b,'bo')
# plt.show()


# t1 = np.arange(0,5,0.1)
# t2 = np.arange(0,5,0.02)
# print(t1)
# print(t2)
#
# # 한 화면에 두개의 값을 넣기위해 subplot 사용
# # 2행 1열로 나눠줘, 그리고 1번째 공간에 지금 그릴 챠트를 그려줘
# plt.subplot(211)
# plt.plot(t1,'ro')
# plt.subplot(212)
# plt.plot(t2,'bo')
# plt.show()

# # figure은 도화지를 만들어 달라는 뜻
# # t1의 데이터를 가지고 차트를 만들어주세요
# plt.figure(1)
# plt.plot(t1, 'bo')
#
# plt.figure(2)
# plt.plot(t2, 'ro')
#
# plt.show()














# height = np.array([170,180,160,185,167])
# weight = np.array([80,100,65,105,73])

# plt.plot(weight,height,'bo')
# plt.xlim(0,150)
# plt.ylim(100,200)
# plt.show()

# # 연습) x의 범위가 -10 에서 10일때 x제곱값을 차트로 그려주세요
# x = np.arange(-10,10)
# y = x**2
# print(x)
# print(y)
# '''
# x = [-10  -9  -8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   8   9]
# y = [100  81  64  49  36  25  16   9   4   1   0   1   4   9  16  25  36  49  64  81]
# '''
#
# plt.plot(x,y,'bo')
# plt.xlim(-10,10)
# plt.show()





# qty = np.array([60,100,30,40,150])
# plt.plot(qty)
# plt.show()
'''
       월    화    수    목    금
딸기  1000  1100  1000  900  1500
수박  80     80    100   50   40
포도  60     70    40    50   60
'''
# qty = np.array([[1000,1100,1000,900,1500],[80,80,100,50,40],[60,70,40,50,60]])

# 수박에 대한 판매량의 정보를 차트로 나타내 봅니다.

# plt.plot(qty[1])
# plt.plot(qty[1],'ro')
# plt.show()


# 수박에 대한 평균판매량을 계산하고
# 평균판매량과 각각의 판매량의 차액을 차트로 나타내 봅니다.
# avg = np.average(qty[1])
# np.mean(qty[1]) 같은뜻
'''
70.0
'''
# abs 는 양수를 음수로 변경해줌

# a = abs(qty[1] - np.mean(qty[1]))
# broad casting
# print(a)
# plt.plot(a,'bo')
# plt.ylim(0,100)
# plt.xlim(0,100)
# plt.show()

