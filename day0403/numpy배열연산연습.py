import numpy as np

name = ['홍길동','강감찬','이순신','유관순','김유신']
score = [80,60,100,40,70]

#60점 이상이면 합격입니다.
# 합격한 학생들의 이름을 출력 해 봅니다.
for i in range(len(score)):
    if score[i] >= 60:
        print(name[i])
n = np.array(name)
s = np.array(score)

s = s >= 60
print(s)
'''
[ True  True  True False  True]
'''
print(n[s])
'''
['홍길동' '강감찬' '이순신' '김유신']
boolean 값으로 바뀐 s 를 n배열에 넣어준다.
'''

name = np.array(name)
score = np.array(score)
print(name[score >= 60])
'''
['홍길동' '강감찬' '이순신' '김유신']
n[s >= 60] 은 안됨 궁금! 
'''

