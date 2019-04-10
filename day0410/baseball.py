# 연습) baseball을 읽어와 팀별로 챔피언한 횟수를 출력해 봅니다.

import numpy as np
import pandas as pd

f = pd.read_csv('../Data/baseball2.txt',sep=',', engine='python')
# print(f)
#                    구하고자하는것        ~~별로            함수(식)
data = f.pivot_table(values='Wins', index='Champion', aggfunc='count')
# print(data)

sortdata = data.sort_values(by='Wins',ascending=False)
# print(sortdata)
'''
                        Wins
Champion                    
New York Yankees           9
Boston Red Sox             7
Philadelphia Athletics     5
 St. Louis Cardinals       4
 New York Giants           4
San Francisco Giants       3
Chicago Cubs               3
 Chicago White Sox         3
 Toronto Blue Jays         2
 Cincinatti Reds           2
 Minnesota Twins           2
 Florida Marlins           2
 Oakland Athletics         1
Boston Americans           1
Pittsburgh Pirates         1
 Cleveland Indians         1
Kansas City Royals         1
 Los Angeles Dodgers       1
Atlanta Braves             1
 Philadelphia Phillies     1
Arizona Diamondbacks       1
Anaheim Angels             1
 Washington Senators       1
 New York Mets             1
 Pittsburg Pirates         1
 Boston Braves             1
'''
