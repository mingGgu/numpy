import numpy as np

a = ['160.7','180.5','145.5','175.5','160.7','165.8']

# 연습) 파이썬 배열을 numpy배열로 만든 후 그 중 170 이상인 데이터만 뽑아 새로운 numpy배열로 만들어라
an = np.array(a)
print(an)

aint = np.array(a, dtype='float64')
print(aint)

print(aint[aint>=170])



