import numpy as np

# 파이썬 배열을 numpy배열로
# np.array
a=[1,2,3,4,5,6]
print('파이썬 배열: ',a)

an = np.array(a)
print('numpy배열로: ',an)

# numpy배열을 파이썬배열로
# list
b = np.arange(6)
print('numpy배열: ',b)

bl = list(b)
print('파이썬 배열로: ',bl)

