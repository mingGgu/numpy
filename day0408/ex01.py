# 연습) Data폴더의 users.dat. movies.dat, ratings.dat 파일을 읽어들여 하나의 DataFrame으로 만들어 봅니다.
import numpy as np
import pandas as pd

movies = pd.read_csv('../ml-1m/movies.dat',sep='::',engine='python',header=None, names=['movieid','title','ganre'])
# print(movies)
'''
         1  ...     Animation|Children's|Comedy
0        2  ...    Adventure|Children's|Fantasy
1        3  ...                  Comedy|Romance
2        4  ...                    Comedy|Drama
3        5  ...                          Comedy
4        6  ...           Action|Crime|Thriller
'''

# print(movies.head(1))
'''
   1 Toy Story (1995)   Animation|Children's|Comedy
0  2   Jumanji (1995)  Adventure|Children's|Fantasy
'''

# print(df2.head(1))
'''
   0                 1                            2
0  1  Toy Story (1995)  Animation|Children's|Comedy
'''

# names=['movieid','title','ganre']
print(movies)
'''
      movieid  ...                           ganre
0           1  ...     Animation|Children's|Comedy
1           2  ...    Adventure|Children's|Fantasy
2           3  ...                  Comedy|Romance
3           4  ...                    Comedy|Drama
4           5  ...                          Comedy
5           6  ...           Action|Crime|Thriller
'''

users = pd.read_csv('../ml-1m/users.dat',sep='::',engine='python',header=None, names=['userid','gender','age','jop','zipcode'])
print(users)
'''
      userid gender  age  jop zipcode
0          1      F    1   10   48067
1          2      M   56   16   70072
2          3      M   25   15   55117
3          4      M   45    7   02460
4          5      M   25   20   55455
'''

ratings = pd.read_csv('../ml-1m/ratings.dat',sep='::',engine='python',header=None, names=['userid','movieid','rating','timestamp'])
print(ratings)
'''
         userid  movieid  rating  timestamp
0             1     1193       5  978300760
1             1      661       3  978302109
2             1      914       3  978301968
3             1     3408       4  978300275
4             1     2355       5  978824291

'''

#-------------- 병합한 후!---------------------

df = pd.merge( pd.merge(ratings,movies),users)
# print(df)
'''
        userid  movieid  rating  timestamp  ... gender age jop  zipcode
0             1     1193       5  978300760  ...      F   1  10    48067
1             1      661       3  978302109  ...      F   1  10    48067
2             1      914       3  978301968  ...      F   1  10    48067
3             1     3408       4  978300275  ...      F   1  10    48067
4             1     2355       5  978824291  ...      F   1  10    48067
'''