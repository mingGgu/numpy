import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

path = "c:/Windows/Fonts/malgun.ttf"
rc('font',family=font_manager.FontProperties(fname=path).get_name())

tmp_data = []

with open('./Data/2016_GDP.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(':')

        tmp_data.append(cols)

del tmp_data[0]

gp_title = []
gp_val = []
for val in tmp_data:
    gp_title.append(val[1])
    gp_val.append(val[2].replace(",",""))

gp_title=np.array(gp_title)
gp_val = np.array(gp_val, dtype=np.int)

idx = gp_val.argsort()[::-1]

x = gp_title[idx][:10]
y = gp_val[idx][:10]

# plt.barrh(range(10), y, tick_label=x)
plt.barh(range(10), y, tick_label=x)
plt.title('2016년 국가별 GDP')
plt.show()
