from sklearn import preprocessing
import numpy as np

# 문자를 이진화 배열로 만들어 봅시다.
# ===> LabelBinarizer

x = ['yes','no','yes']
lb = preprocessing.LabelBinarizer()
bn = lb.fit_transform(x)
print(bn)
'''
[[1]
 [0]
 [1]]
yes = 1 / no = 0
'''

x1 = ['yes','no','yes','cancle']
lb = preprocessing.LabelBinarizer()
bn = lb.fit_transform(x1)
print(bn)
'''
[[0 0 1]    : yes
 [0 1 0]    : no
 [0 0 1]    : yes
 [1 0 0]]   : cancle
'''

r = np.array([[0,0,1]])
# 다시 문자로 바꾸기
s = lb.inverse_transform(r)
print(s)
'''
['yes']
'''

d = lb.fit_transform(x1)
print(d)
'''
[[0 0 1]
 [0 1 0]
 [0 0 1]
 [1 0 0]]
'''

z = lb.inverse_transform(d)
print(z)
'''
['yes' 'no' 'yes' 'cancle']
'''

y = ['paris','tokyo','london','paris']
lb1 = preprocessing.LabelBinarizer()
bb = lb1.fit_transform(y)
print(bb)
'''
[[0 1 0]    : paris
 [0 0 1]    : tokyo
 [1 0 0]    : london
 [0 1 0]]   : paris
'''

r1 = np.array([[1,0,0]])
result1 = lb1.inverse_transform(r1)
print(result1)
'''
['london']
'''























