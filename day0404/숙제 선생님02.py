import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc, colors
import csv

f = open('./Data/2016_GDP.txt','r',encoding='utf-8')
f.readline()

names, money = [],[]

# 파일이있는 변수를 넣어주고, 구분자(delimiter)를 넣어준다.
list = csv.reader(f, delimiter=':')
print(list)
'''
<_csv.reader object at 0x0000000013538A08>
'''
for row in list:
    names.append(row[1])
    money.append(row[2].replace(",",""))
    # print(row)
    '''
    ['1', '룩셈부르크', '101,715']
    ['2', '스위스', '78,245']
    ['3', '노르웨이', '73,450']
    ['4', '마카오', '68,401']
    ['5', '아이슬란드', '67,570']
    '''
f.close()

# 한글글꼴 설정
rc('font', family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf').get_name())

money = np.array(money, dtype='int32')

# plt.bar(range(10), money[:10])
# plt.bar(range(10), money[:10],color='b')
plt.bar(range(10), money[:10],color=colors.TABLEAU_COLORS)
plt.title('GDP 상위 10개의 나라')
# 축의 몇개야~, 값, 회전
plt.xticks(range(10), names[:10],rotation='90')
plt.show()
