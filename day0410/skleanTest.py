from sklearn import preprocessing
import numpy as np

age = [26,20,26,29]
addr = ['서울','마산','서울','대전','광주']

b_age = preprocessing.LabelBinarizer().fit_transform(age)
print(b_age)
'''
[[0 1 0]    :   26
 [1 0 0]    :   20
 [0 1 0]    :   26
 [0 0 1]]   :   29
'''

b_addr= preprocessing.LabelBinarizer().fit_transform(addr)
print(b_addr)
'''
[[0 0 0 1]  :   서울
 [0 0 1 0]  :   마산
 [0 0 0 1]  :   서울
 [0 1 0 0]  :   대전
 [1 0 0 0]] :   광주
'''

# 데이터의 value(값)의 수만큼 feature(속성)이 만들어지고 해당 속성에 1을 주고 나머지는 0으로 채운다.
# 여기선 서울,마산,서울,대전,광주 총 4가지라서 이진수도 4자리로 나온다.
