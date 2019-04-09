import ex02
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = ex02.getMovie()

# 연습) 영화이름별로 투표건수를 출력
# print(df)

title_count = df.pivot_table(values='userid', index='title', aggfunc='count')
# values에 들어가는건 rating도 상관없음
# print(title_count)
'''       userid     
                                                userid
title                                                 
$1,000,000 Duck (1971)                              37
'Night Mother (1986)                                70
'Til There Was You (1997)                           52
'burbs, The (1989)                                 303
...And Justice for All (1979)                      199
1-900 (1994)                                         2
10 Things I Hate About You (1999)                  700
101 Dalmatians (1961)                              565
101 Dalmatians (1996)                              364
12 Angry Men (1957)                                616
13th Warrior, The (1999)                           750
187 (1997)                                          55
2 Days in the Valley (1996)                        286
20 Dates (1998)                                    139
20,000 Leagues Under the Sea (1954)                575
200 Cigarettes (1999)                              181
2001: A Space Odyssey (1968)                      1716
2010 (1984)                                        470
24 7: Twenty Four Seven (1997)                       5
24-hour Woman (1998)                                 9
28 Days (2000)                                     505
3 Ninjas: High Noon On Mega Mountain (1998)         47
3 Strikes (2000)                                     4
301, 302 (1995)                                      9
39 Steps, The (1935)                               253
400 Blows, The (Les Quatre cents coups) (1959)     187
42 Up (1998)                                        88
52 Pick-Up (1986)                                  140
54 (1998)                                          259
7th Voyage of Sinbad, The (1958)                   258
...                                                ...
Wrongfully Accused (1998)                          123
Wyatt Earp (1994)                                  270
X-Files: Fight the Future, The (1998)              996
X-Men (2000)                                      1511
X: The Unknown (1956)                               12
Xiu Xiu: The Sent-Down Girl (Tian yu) (1998)        69
Yankee Zulu (1994)                                   2
Yards, The (1999)                                   77
Year My Voice Broke, The (1987)                     27
Year of Living Dangerously (1982)                  391
Year of the Horse (1997)                             4
Yellow Submarine (1968)                            399
Yojimbo (1961)                                     215
You Can't Take It With You (1938)                   77
You So Crazy (1994)                                 13
You've Got Mail (1998)                             838
Young Doctors in Love (1982)                        79
Young Frankenstein (1974)                         1193
Young Guns (1988)                                  562
Young Guns II (1990)                               369
Young Poisoner's Handbook, The (1995)               79
Young Sherlock Holmes (1985)                       379
Young and Innocent (1937)                           10
Your Friends and Neighbors (1998)                  109
Zachariah (1971)                                     2
Zed & Two Noughts, A (1985)                         29
Zero Effect (1998)                                 301
Zero Kelvin (Kj�rlighetens kj�tere) (1995)           2
Zeus and Roxanne (1997)                             23
eXistenZ (1999)                                    410
'''


# 연습)평가 건수가 100개 이상인 영화제목을 출력

# print(title_count['userid'] >= 100)
'''
title
$1,000,000 Duck (1971)                            False
'Night Mother (1986)                              False
'Til There Was You (1997)                         False
'burbs, The (1989)                                 True
...And Justice for All (1979)                      True
1-900 (1994)                                      False
10 Things I Hate About You (1999)                  True
101 Dalmatians (1961)                              True
101 Dalmatians (1996)                              True
12 Angry Men (1957)                                True
13th Warrior, The (1999)                           True
187 (1997)                                        False
2 Days in the Valley (1996)                        True
'''

title_100 = title_count[title_count['userid'] >= 100]
# print(title_100)
'''
                                                  userid
title                                                   
'burbs, The (1989)                                   303
...And Justice for All (1979)                        199
10 Things I Hate About You (1999)                    700
101 Dalmatians (1961)                                565
101 Dalmatians (1996)                                364
12 Angry Men (1957)                                  616
13th Warrior, The (1999)                             750
2 Days in the Valley (1996)                          286
20 Dates (1998)                                      139
20,000 Leagues Under the Sea (1954)                  575
200 Cigarettes (1999)                                181
.
.
.
[2019 rows x 1 columns] 
# 2019개가 나옴
'''

title_500 = title_count[title_count['userid'] >= 500]
# print(title_500)
'''
                                                    userid
title                                                     
10 Things I Hate About You (1999)                      700
101 Dalmatians (1961)                                  565
12 Angry Men (1957)                                    616
13th Warrior, The (1999)                               750
20,000 Leagues Under the Sea (1954)                    575
2001: A Space Odyssey (1968)                          1716
28 Days (2000)                                         505
Abyss, The (1989)                                     1715
Ace Ventura: Pet Detective (1994)                      766
.
.
.
[618 rows x 1 columns]
'''

# 연습) 평가건수가 500개 이상인 영화제목을 내림차순으로 정렬
title_500_sort = title_500.sort_values(by='userid', ascending=False) # ascending은 default값으로 오름차순을 가진다.
print(title_500_sort)
'''
                                                    userid
title                                                     
American Beauty (1999)                                3428
Star Wars: Episode IV - A New Hope (1977)             2991
Star Wars: Episode V - The Empire Strikes Back ...    2990
Star Wars: Episode VI - Return of the Jedi (1983)     2883
Jurassic Park (1993)                                  2672
Saving Private Ryan (1998)                            2653
Terminator 2: Judgment Day (1991)                     2649
Matrix, The (1999)                                    2590
Back to the Future (1985)                             2583
.
.
.
Emma (1996)                                            501
Postino, Il (The Postman) (1994)                       501
Last Action Hero (1993)                                500
'''








