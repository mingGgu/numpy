# 연습) baseball.txt파일을 DataFrame으로 읽어들인다
# 연습) 팀별로 우승한 횟수를 출력해 봅니다.
import numpy as pn
import pandas as pd


df = pd.read_csv('../Data/baseball.txt')
# print(df)

r = df.pivot_table(values='Champion',index='Wins',aggfunc='count')
print(r)