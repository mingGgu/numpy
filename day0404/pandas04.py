import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/scores.csv')

# pandas의 DataFrame에서 행에 접근하는 방법은 loc 이나 iloc 함수를 이용하여 접근한다.
# key값을 부여하지 않고 행에 접근하려면 index로 접근합니다.
# 이때는 loc나 iloc을 사용하는데에 차이가 없다. 그러나 key값을 부여했을때는 달라짐
# index로 접근할 때는 iloc을 사용
# key로 접근할 때는 loc을 사용

print(df.loc[2].values)
print(df.iloc[2].values)
'''
[1 'ben' 95 59 96 88]
[1 'ben' 95 59 96 88]
'''

# 학생의 이름을 DataFrame의 key로 설정
df.index = df['name']
print(df)
'''
        class    name  kor  eng  mat  bio
name                                     
adam        1    adam   67   87   90   98
andrew      1  andrew   45   45   56   98
ben         1     ben   95   59   96   88
clark       1   clark   65   94   89   98
dan         1     dan   45   65   78   98
noel        1    noel   78   76   98   89
paul        2    paul   87   67   65   56
walter      2  walter   89   98   78   78
oscar       2   oscar  100   78   56   65
martin      2  martin   99   89   87   87
hugh        2    hugh   98   45   56   54
henry       2   henry   65   89   87   78
'''

# 기존에 있던 name은 중복되니 삭제해준다
del df['name']
print(df)
'''
        class  kor  eng  mat  bio
name                             
adam        1   67   87   90   98
andrew      1   45   45   56   98
ben         1   95   59   96   88
clark       1   65   94   89   98
dan         1   45   65   78   98
noel        1   78   76   98   89
paul        2   87   67   65   56
walter      2   89   98   78   78
oscar       2  100   78   56   65
martin      2   99   89   87   87
hugh        2   98   45   56   54
henry       2   65   89   87   78
'''
# --------------------------------------------------------------------------

print('연습1) henry의 정보를 출력해 봅니다.')
print(df.loc['henry'].values)
print(df.iloc[-1].values)
'''
[ 2 65 89 87 78]
'''

# print('연습2)andrew부터 paul까지의 정보를 출력해 봅니다.')

print(df.loc['andrew':'paul'])
'''
#loc 방법 -----------------------
        class  kor  eng  mat  bio
name                             
andrew      1   45   45   56   98
ben         1   95   59   96   88
clark       1   65   94   89   98
dan         1   45   65   78   98
noel        1   78   76   98   89
paul        2   87   67   65   56
'''
print(df.iloc[1:7].values)
'''
#iloc 방법 ----------------------
[[ 1 45 45 56 98]
 [ 1 95 59 96 88]
 [ 1 65 94 89 98]
 [ 1 45 65 78 98]
 [ 1 78 76 98 89]
 [ 2 87 67 65 56]]
'''

# print('연습3)adam dan walter의 정보를 출력해봅니다.')

print(df.loc[['adam','dan','walter']])

ps = ['adam','dan','walter']
print(df.loc[ps])

'''
        class  kor  eng  mat  bio
name                             
adam        1   67   87   90   98
dan         1   45   65   78   98
walter      2   89   98   78   78
'''

# print('연습4)앞에서 5번째 학생들의 국어점수를 출력해봅니다.')

print(df.iloc[:5,1])
print(df.iloc[:5]['kor'])
print(df.loc[:'dan','kor'])
'''
name
adam      67
andrew    45
ben       95
clark     65
dan       45
Name: kor, dtype: int64
'''

# print('연습5) 앞에서 5번째 학생들의 국어,수학점수를 출력해 봅니다.')

print(df.iloc[:5,1:3])
print(df.iloc[:5][['kor','mat']])
'''
        kor  eng
name            
adam     67   87
andrew   45   45
ben      95   59
clark    65   94
dan      45   65
'''

# print('연습6)adam dan walter의 bio를 제외한 과목의 점수를 출력')

print(df.loc[['adam','ben','walter'],'kor':'mat'])
names = ['adam','dan','walter']
subjects = ['kor','eng','mat']
print(df.loc[names,subjects])
print(df.loc[names][subjects])
print(df.iloc[[1,4,7], 1:4])
names1 = [0,4,7]
print(df.iloc[names1, 1:-1])
'''
name                 
andrew   45   45   56
dan      45   65   78
walter   89   98   78
'''