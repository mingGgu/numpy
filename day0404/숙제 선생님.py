import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc, colors

# 여기서 r은 읽기위한 모드로 열것이다. 라는 뜻
f = open('./Data/2016_GDP.txt','r',encoding='utf-8')
# 제목인 맨 윗줄 한줄은 버리고( readline은 한줄만 읽어오기때문에 )
f.readline()
# 모두 읽어줘. 라는 뜻
list = f.readlines()
# 나라이름과 달라를 추출해서 각각 담으려고한다.
names = []
money = []
for row in list:
    # 한줄한줄 뽑는식
    # print(row)
    '''
    1:룩셈부르크:101,715
    2:스위스:78,245
    3:노르웨이:73,450
    '''
    row = row.split(':')
    # 콜론을 지우니 개행문자도 나타남
    # print(row)
    '''
    ['1', '룩셈부르크', '101,715\n']
    ['2', '스위스', '78,245\n']
    ['3', '노르웨이', '73,450\n']
    '''
    names.append(row[1])
    # strip은 개행문자 없애라는 명령
    money.append(row[2].strip().replace(",",""))
print(names)
# ['룩셈부르크', '스위스', '노르웨이', '마카오',. . . ]
print(money)
# ['101715', '78245', '73450', '68401', . . .]
# money가 순위대로 되어있다.
money = np.array(money, dtype='int32')
# 한글글꼴 설정
rc('font', family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf').get_name())

# plt.bar(range(10), money[:10])
# plt.bar(range(10), money[:10],color='b')
plt.bar(range(10), money[:10],color=colors.TABLEAU_COLORS)
plt.title('GDP 상위 10개의 나라')
# 축의 몇개야~, 값, 회전
plt.xticks(range(10), names[:10],rotation='90')
plt.show()
