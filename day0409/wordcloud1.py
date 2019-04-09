import numpy as np
import pandas as pd
from matplotlib import font_manager,rc
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import ImageColorGenerator

r = open('../Data/moon.txt')
moon = r.read()
cloud = WordCloud(font_path='C:\Windows\Fonts\Cambria/DXKPMB-KSCpc-EUC-H.ttf',min_font_size=10,max_font_size=100,font_step=10,max_words=100,background_color='white')
word_count = cloud.process_text(moon)

# dictionary의 value를 기준으로 정렬하려면
import operator
sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1))[::-1]
sorted_word_count = sorted_word_count[:20]
print(sorted_word_count)

delWord = ['것입니다','우리는','함께','새로운','우리가','있습니다','우리의','국민의','새로운 100년은','100년','위해','것이','바로','있는','우리','오늘','합니다','않고']
moon = moon.replace('100년은','100년')
moon = moon.replace('한반도의','한반도')
for dw in delWord:
    moon = moon.replace(dw , '')

world_map = np.array(Image.open('../Data/world_map.png'))
image_colors = ImageColorGenerator(world_map)

cloud1 = WordCloud(font_path='C:\Windows\Fonts\Cambria/DXKPMB-KSCpc-EUC-H.ttf',
                   relative_scaling=0.2,
                   mask=world_map,
                   min_font_size=1,
                   max_font_size=40,
                   font_step=10,
                   max_words=100,
                   background_color='white').generate(moon)
plt.axis('off')
# plt.imshow(cloud1,interpolation='bilinear')
plt.imshow(cloud1.recolor(color_func=image_colors),interpolation='bilinear')
plt.show()












# 연습) 문재인 대통령의 연설문을 워드클라우드로 표현해 봅니다.
# r = open('../Data/moon.txt')
# moon = r.read()
# cloud = WordCloud(font_path='C:\Windows\Fonts\Cambria/DXKPMB-KSCpc-EUC-H.ttf',background_color='white')
# word_count = cloud.process_text(moon)
# print(word_count)
#
# # dictionary의 value를 기준으로 정렬하려면
# import operator
# sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1))[::-1]
# sorted_word_count = sorted_word_count[:20]
# print(sorted_word_count)
# '''
# [('것입니다', 23), ('우리는', 13), ('함께', 12), ('우리', 11), ('새로운', 9), ('우리가', 9), ('있습니다', 8),
#  ('우리의', 7), ('100년', 7), ('국민의', 6), ('세계', 6), ('새로운 100년은', 5), ('신한반도체제', 5),
#  ('한반도의', 5), ('평화의', 5), ('위해', 5), ('것이', 5), ('바로', 5), ('있는', 5), ('한반도', 5)]
# '''
#
# delWord = ['것입니다','우리는','함께','새로운','우리가','있습니다','우리의','국민의','새로운 100년은','100년','위해','것이','바로','있는','우리','오늘','합니다','않고']
# moon = moon.replace('100년은','100년')
# moon = moon.replace('한반도의','한반도')
# for dw in delWord:
#     moon = moon.replace(dw , '')
#
# cloud1 = cloud.generate(moon)
# plt.axis('off')
# plt.imshow(cloud1)
# plt.show()
# moon = moon.replace('우리가','')
# moon = moon.replace('것입니다.','')
# moon = moon.replace('함께','')
#
# delWord = ['것입니다.','우리가','함께','우리는','우리','우리의','있습니다','오늘','시작했습니다','100년','바로','것이','이제','위해','합니다']
# for dw in delWord:
#     moon = moon.replace(dw ,'')
#
# wc = WordCloud(font_path='C:\Windows\Fonts\Cambria/DXKPMB-KSCpc-EUC-H.ttf',background_color= 'white', width=800, height=600).generate(moon)
# rc('font',family=font_manager.FontProperties(fname='C:\Windows\Fonts/DXMSubtitlesM-KSCpc-EUC-H.ttf').get_name())
# plt.title('문제인 대통령 연설문 시각화')
# plt.imshow(wc)
# # x축 y축의 범위(숫자) 삭제
# plt.axis('off')
# plt.show()

# 연습) 위의 연설문에서 데이터 분석에 의미 없는 단어를 모두 제거하고
# 다시 워드클라우드로 표현해 봅니다.

# 단어별 빈도수를 먼저 파악하고 빈도수별 내림차순 정렬하여 필요없는 단어를 파악하고 싶다.
# r = open('../Data/i_have_a_dream.txt')
# data = r.read()
# r.close()
# print(data)
# # 단어별 빈도수를 워드클라우드로 표현해 봅시다.
# colud1 = WordCloud().generate(data) #문자열 데이터를 가지고 워드클라우드 객체생성
# print(colud1)
# print(type(colud1))
# '''
# <wordcloud.wordcloud.WordCloud object at 0x000000001391A208>
# <class 'wordcloud.wordcloud.WordCloud'>
# '''
#
# # 워드클라우드 객체에 해당하는 이미지 생성
# plt.imshow(colud1)
#
# # 워드클라우드에서는 차트의 축을 없애는것이 보기 좋을 거 같아요
# plt.axis('off') #챠트의 x,y축을 없애 주세요
# plt.show()      #워드클라우드 보여주세요

















