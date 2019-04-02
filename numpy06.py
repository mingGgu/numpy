import numpy as np

# a = np.arange(3)
# print(a)
# print(a+1)      #broad casting
# print(a>1)
# print(a[a>1])   #True index에 해당하는 값만 나온다.

# 행이나 열 중 하나를 정해주고 -1을 붙여주면 나머지는 너가 알아서 해줘 라는 뜻
b = np.arange(6).reshape(-1,3)
c = np.arange(6).reshape(2,-1)
d = np.arange(6).reshape(2,3)

print(b)
print('')
print(b+1)
print('')

print(b>1)      #b의 요소만큼 비교여하여 True False를 반환한다.
print('')

print(b[0])
print(b[0][0])
print('')

print(b[b>1])       # broad casting의 True요소만 출력



