import numpy as np
import pandas as pd
import xlrd

df = pd.read_excel('../Data/MLB World Series Champions_ 1903-2016.xlsx')

# 최다챔피언한 5위안에 드는 팀을 출력, 우승한 횟수가 동일한 팀이 여러팀인 경우 모두 출력해 주세요
win_count = df.pivot_table(values='Wins',index='Champion',aggfunc='count')
sorted_win_count = win_count.sort_values(by='Wins',ascending=False)
print(sorted_win_count)

# 우승한 횟수를 중복이 되지 않도록 만듭니다.  =>  r

r = sorted_win_count['Wins'].unique()
print(r)
'''
[27 11  7  5  4  3  2  1]
'''

# 그 중에 5번째 값을 뽑아온다.(top5를 뽑아야하니까)     =>  min

min = r[4]
print(min)
'''
4
'''

# sorted_win_count의 Wins가 그 5번째 값 이상인 값을 뽑는다.    =>  Wins가 min이상 되는 데이터를 출력
top_5 = sorted_win_count[sorted_win_count['Wins'] >= min]
print(top_5)
print(len(top_5))
'''
                        Wins
Champion                    
New York Yankees          27
St. Louis Cardinals       11
Boston Red Sox             7
Los Angeles Dodgers        5
Cincinatti Reds            5
New York Giants            5
Philadelphia Athletics     5
Detroit Tigers             4
Oakland Athletics          4
Pittsburgh Pirates         4

10
'''











# df = pd.read_excel('../Data/MLB World Series Champions_ 1903-2016.xlsx')
# # print(df.head())
# '''
#    Year           Champion  Wins  Losses  Ties  WinRatio
# 0  1903   Boston Americans    91      47     3     0.656
# 1  1905    New York Giants   105      48     2     0.684
# 2  1906  Chicago White Sox    93      58     3     0.614
# 3  1907       Chicago Cubs   107      45     3     0.700
# 4  1908       Chicago Cubs    99      55     4     0.639
# '''
#
# # print(df.columns)
# # print(df)
#
# champion_cnt = df.pivot_table(values='Wins',index='Champion',aggfunc='count')
# # print(champion_cnt)
#
# # 연습) 팀별로 평균 승률 출력
# champion_WR = df.pivot_table(values='WinRatio',index='Champion',aggfunc='mean')
# # print(champion_WR)
#
# # 연습) 평균 승률이 높은 상위 5개의 팀 출력
# champion_top = champion_WR.sort_values(by='WinRatio',ascending=False)
# print(champion_top.head(5))
# '''
#                         WinRatio
# Champion
# Pittsburg Pirates       0.721000
# Philadelphia Athletics  0.664600
# Chicago Cubs            0.659333
# Boston Americans        0.656000
# New York Mets           0.642000
# '''
#
# # 연습) 2000년 이후의 데이터중 평균승률이 가장 높은 상위 5개의 팀
# # year = df['Year'] >= 2000
# # print( df[year])
# df_2000 = df[df['Year'] >= 2000]
# '''
#      Year               Champion  Wins  Losses  Ties  WinRatio
# 95   2000       New York Yankees    87      74     0     0.540
# 96   2001   Arizona Diamondbacks    92      70     0     0.568
# 97   2002         Anaheim Angels    99      63     0     0.611
# 98   2003        Florida Marlins    91      71     0     0.562
# 99   2004         Boston Red Sox    98      64     0     0.605
# 100  2005      Chicago White Sox    99      63     0     0.611
# 101  2006    St. Louis Cardinals    83      78     0     0.516
# 102  2007         Boston Red Sox    96      66     0     0.593
# 103  2008  Philadelphia Phillies    92      70     0     0.568
# 104  2009       New York Yankees   103      59     0     0.636
# 105  2010   San Francisco Giants    92      70     0     0.568
# 106  2011    St. Louis Cardinals    90      72     0     0.556
# 107  2012   San Francisco Giants    94      68     0     0.580
# 108  2013         Boston Red Sox    97      65     0     0.599
# 109  2014   San Francisco Giants    88      74     0     0.543
# 110  2015     Kansas City Royals    95      67     0     0.586
# 111  2016           Chicago Cubs   103      58     1     0.639
# '''
#
# champion_2000 = df_2000.pivot_table(values='WinRatio',index='Champion',aggfunc='mean')
# sorted_wins = champion_2000.sort_values(by='WinRatio',ascending=False)
# print(sorted_wins.head(5))
# '''
# Champion
# Chicago Cubs          0.639
# Anaheim Angels        0.611
# Chicago White Sox     0.611
# Boston Red Sox        0.599
# New York Yankees      0.588
# '''
#
# # 연습)우승한 횟수가 100승이상인 팀을 출력해주세요
# Wins_100 = df[df['Wins'] >= 100]
# df_100_team = Wins_100['Champion'].unique()
# # print(df_100_team)
# '''
# ['New York Giants' 'Chicago Cubs' 'Pittsburg Pirates'
#  'Philadelphia Athletics' 'Boston Red Sox' 'Chicago White Sox'
#  'New York Yankees' 'St. Louis Cardinals' 'Cincinatti Reds'
#  'Detroit Tigers' 'New York Mets' 'Baltimore Orioles']
# '''
#
# # print(len(df_100_team))
# '''
# 12
# '''
#
# # 연습)New York Yankees 팀이 처음 우승한 연도와 마지막으로 우승한 연도를 출력
#
# NYY = df[df['Champion'] == 'New York Yankees']
#
# # 방법1 ------------------------------------------------
# first_win = NYY.head(1)
# last_win = NYY.tail(1)
# # print(first_win['Year'],last_win['Year'])
# '''
# Name: Year, dtype: int64 104    2009
# Name: Year, dtype: int64
# '''
#
# # 방법2 ------------------------------------------------
# sort_df_nyy = NYY.sort_values(by='Year')
# first_win , last_win = sort_df_nyy.iloc[0]['Year'],sort_df_nyy.iloc[-1]['Year']
# # print(first_win, last_win)
# '''
# 1923 2009
# '''
#
# # 방법3 ------------------------------------------------
# firstYear, lastYear = NYY['Year'].min() , NYY['Year'].max()
# # print(firstYear, lastYear)
# '''
# 1923 2009
# '''
#
# # 연습) 월드시리즈가 열리지 않은 연도를 출력해 봅니다.
#
# # 방법1 --------------------------------------------------
# all_Year = np.arange(1903,2017)
# world_not_year=[]
# g_Year = df['Year']
# print(all_Year)
# print(g_Year)
#
# i = 0
# for a in all_Year:
#      yy = g_Year[i]
#      if a != yy:
#          world_not_year.append(a)
#          # 다음 연도로 돌아가~
#          continue
#      i = i + 1
# print(world_not_year)
# '''
# [1904, 1994]
# '''
# # 방법2 --------------------------------------------------
# # 매년 열리니까 앞의 연도와 다음 연도의 차이가 1보다 크면 앞의 연도의 +1 한 연도에만 경기가 열리지 않았은것.
# not_year = []
# g_year = df['Year']
#
# # 2016년은 다음연도가 없어서 비교할 수 없기때문에 -1을 해주어서 2015년 까지만 닿도록 한다.
# for i in range(len(g_year)-1):
#     if g_year[i+1] - g_year[i] > 1:
#         not_year.append(g_year[i]+1)
# print(not_year)
# '''
# [1904, 1994]
# '''
#
# # 타입을 일치시켜야함(numpy로 일치시킴)
# all_Year = np.arange(1903,2017)
# g_Year = np.array(df['Year'])
#
# # setdiff1d => 차집합을 구해준다.
# not_year = np.setdiff1d(all_Year, g_Year)
# print(not_year)
# '''
# [1904 1994]
# '''
#
# not_year1 = list(set(all_Year) - set(g_Year))
# print(not_year1)
# '''
# [1904, 1994]
# # 순서 보존 안됨
# '''
#
# s = set(g_Year)
# not_year2 = [x for x in all_Year if x not in s]
# print(not_year2)
# '''
# [1904, 1994]
# # 순서 보존됨
# '''
#
