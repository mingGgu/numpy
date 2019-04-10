import numpy as np
import pandas as pd

member = pd.read_csv('../Data/member.dat')
member['age'] = member['age'].astype(str)
print(member)
print(member.columns)
'''
       id name  age addr
0   tiger  홍길동   20   서울
1    lion  강감찬   40   대전
2     cat  이순신   40   울산
3  monkey  유관순   40   서울

Index(['id', 'name', 'age', 'addr'], dtype='object')
'''

# 연습) addr컬럼과 age 컬럼을 각각 one-hot테이블을 생성해 봅니다.

b_age = pd.get_dummies(member['age'])
print(b_age)
'''
   20  40
0   1   0
1   0   1
2   0   1
3   0   1
'''
b_addr = pd.get_dummies(member['addr'])
print(b_addr)
'''
   대전  서울  울산
0   0   1   0
1   1   0   0
2   0   0   1
3   0   1   0
'''

# pandas의 get_dummies는 만약 1차원배열을 매개변수로 받으면 그것이 숫자이던 문자이던 one-hot encoding을 해준다.
# 그런데 만약 dataframe을 매개변수로 받으면 숫자를 제외하고 나머지를 encoding해줌
# 숫자도 포함하여 one-hot encoding을 하려면 DataFrame의 숫자의 속성을 문자로 변경한 후 해줘야한다.
# 숫자를 문자로 바꾸는 함수     => 데이터프레임['속성명'] = 데이터프레임['속성명'].astype(str)

b_member = pd.get_dummies(member)
print(b_member)
'''
   id_cat  id_lion  id_monkey  id_tiger  ...  age_40  addr_대전  addr_서울  addr_울산
0       0        0          0         1  ...       0        0        1        0
1       0        1          0         0  ...       1        1        0        0
2       1        0          0         0  ...       1        0        0        1
3       0        0          1         0  ...       1        0        1        0

[4 rows x 13 columns]

13개의 컬럼이 만들어지는 이유는 속성하나하나 이진화하여 컬럼을 만들어주기때문에
'''