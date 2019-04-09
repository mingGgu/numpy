import numpy as np
import pandas as pd
import ex02

df = ex02.getMovie()
cnt_500 = ex02.get_500_movie()
# print(cnt_500.columns)
# print(cnt_500.index)
'''
Index(['userid'], dtype='object')
Index(['American Beauty (1999)', 'Star Wars: Episode IV - A New Hope (1977)',
       'Star Wars: Episode V - The Empire Strikes Back (1980)',
       'Star Wars: Episode VI - Return of the Jedi (1983)',
       'Jurassic Park (1993)', 'Saving Private Ryan (1998)',
       'Terminator 2: Judgment Day (1991)', 'Matrix, The (1999)',
       'Back to the Future (1985)', 'Silence of the Lambs, The (1991)',
       ...
       'Ice Storm, The (1997)', 'Halloween (1978)',
       'Peggy Sue Got Married (1986)', '28 Days (2000)', 'Body Heat (1981)',
       'Alien Nation (1988)', 'Guns of Navarone, The (1961)', 'Emma (1996)',
       'Postino, Il (The Postman) (1994)', 'Last Action Hero (1993)'],
      dtype='object', name='title', length=618)
'''

# 평가한 사람이 500명이상인 영화중에 성별별로 영화별로 별점의 평균을 출력

a = df.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
# print(a)

b = a.loc[cnt_500.index]
# print(b)
'''
gender                                                     F         M
title                                                                 
American Beauty (1999)                              4.238901  4.347301
Star Wars: Episode IV - A New Hope (1977)           4.302937  4.495307
Star Wars: Episode V - The Empire Strikes Back ...  4.106481  4.344577
Star Wars: Episode VI - Return of the Jedi (1983)   3.865237  4.069058
Jurassic Park (1993)                                3.579407  3.814197
Saving Private Ryan (1998)                          4.114783  4.398941
Terminator 2: Judgment Day (1991)                   3.785088  4.115367
Matrix, The (1999)                                  4.128405  4.362235
Back to the Future (1985)                           3.932707  4.009259
Silence of the Lambs, The (1991)                    4.271955  4.381944
Men in Black (1997)                                 3.817844  3.719000
Raiders of the Lost Ark (1981)                      4.332168  4.520597
Fargo (1996)                                        4.217656  4.267780
Sixth Sense, The (1999)                             4.477410  4.379944
Braveheart (1995)                                   4.016484  4.297839
Shakespeare in Love (1998)                          4.181704  4.099936
Princess Bride, The (1987)                          4.342767  4.288942
Schindler's List (1993)                             4.562602  4.491415
L.A. Confidential (1997)                            4.106007  4.256678
Groundhog Day (1993)                                3.735562  4.041358
E.T. the Extra-Terrestrial (1982)                   4.089850  3.920264
Star Wars: Episode I - The Phantom Menace (1999)    3.328326  3.431054
Being John Malkovich (1999)                         4.159930  4.113636
Shawshank Redemption, The (1994)                    4.539075  4.560625
Godfather, The (1972)                               4.314700  4.583333
Forrest Gump (1994)                                 4.045031  4.105806
Ghostbusters (1984)                                 3.833962  3.928528
Pulp Fiction (1994)                                 4.071956  4.346839
Terminator, The (1984)                              3.899729  4.205899
Toy Story (1995)                                    4.187817  4.130552
...                                                      ...       ...

[618 rows x 2 columns]
'''

# 연습) 성별로 평점평균의 차이가 가장 많이 나는 영화 5개를 출력 해 봅니다.

# b = a.loc[cnt_500.index]
# b['f-m'] = (b['F'] - b['M']).abs()
# c = b.sort_values(by='f-m',ascending=False)

# 상위 5개 뽑으려면 head를 사용한다.
# print(c)
'''
gender                                         F         M       f-m
title                                                               
Dirty Dancing (1987)                    3.790378  2.959596  0.830782
Good, The Bad and The Ugly, The (1966)  3.494949  4.221300  0.726351
Dumb & Dumber (1994)                    2.697987  3.336595  0.638608
Evil Dead II (Dead By Dawn) (1987)      3.297297  3.909283  0.611985
Grease (1978)                           3.975265  3.367041  0.608224
'''

# 남자가 더 좋아하는 영화 5개
# 남자에서 여자를 빼고 절대값을 붙이지 않는다.

# b['m-f'] = (b['M']-b['F'])
# d = b.sort_values(by='m-f',ascending=False)

# print(d.head(5))
'''
gender                                         F         M       m-f
title                                                               
Good, The Bad and The Ugly, The (1966)  3.494949  4.221300  0.726351
Dumb & Dumber (1994)                    2.697987  3.336595  0.638608
Evil Dead II (Dead By Dawn) (1987)      3.297297  3.909283  0.611985
Caddyshack (1980)                       3.396135  3.969737  0.573602
Animal House (1978)                     3.628906  4.167192  0.538286
'''

# 여자가 더 좋아하는 영화 5개

# b['m-w'] = (b['F']-b['M'])
# e = b.sort_values(by='m-w',ascending=False)

# print(e.head(5))
'''
gender                                        F         M  ...       m-f       m-w
title                                                      ...                    
Dirty Dancing (1987)                   3.790378  2.959596  ... -0.830782  0.830782
Grease (1978)                          3.975265  3.367041  ... -0.608224  0.608224
Rocky Horror Picture Show, The (1975)  3.673016  3.160131  ... -0.512885  0.512885
Mary Poppins (1964)                    4.197740  3.730594  ... -0.467147  0.467147
Sound of Music, The (1965)             4.233677  3.783418  ... -0.450259  0.450259
'''

# 남여 모두 좋아하는 5개
b['f+m'] = (b['F'] + b['M']).abs()
add = b.sort_values(by='f+m',ascending=False)
print(add.head(5))
'''
gender                                                     F  ...       f+m
title                                                         ...          
Close Shave, A (1995)                               4.644444  ...  9.118239
Shawshank Redemption, The (1994)                    4.539075  ...  9.099700
Wrong Trousers, The (1993)                          4.588235  ...  9.066496
Seven Samurai (The Magnificent Seven) (Shichini...  4.481132  ...  9.057760
Schindler's List (1993)                             4.562602  ...  9.054017
'''

# 남여 호불호 갈리지 않는 5개
# c1 = b.sort_values(by='f-m',ascending=True)
# print(c1.head(5))













