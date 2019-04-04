import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

fontName = font_manager.FontProperties(fname='C:/WINDOWS/Fonts/H2GTRE.ttf').get_name()
rc('font', family=fontName)

txt = []
with open('./Data/2016_GDP.txt', 'r', encoding='UTF-8') as data:
    for line in data:
        line = line.strip()
        line = line.split(':')

        for i in range(len(line)):
            line[2] = line[2].replace(',', '')
        txt.append(line)
# 첫번째 행 지우기(제목)
del txt[0]

top_10 = np.array(txt[0:10])
country = top_10[:, 1]
# 맨 마지막 열(-1)
gdp = np.array(top_10[:, -1], dtype=np.int32)

plt.bar(country, gdp)
plt.title("2016년 세계 GDP 상위 10개국")
plt.show()