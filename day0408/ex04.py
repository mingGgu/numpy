import ex02
import numpy as np
import pandas as pd

df = ex02.getMovie()

gender_mean = df.pivot_table(values='rating', index='gender')
gender_mean2 = df.pivot_table(values='rating', index='gender',aggfunc='mean')
gender_sum = df.pivot_table(values='rating', index='gender',aggfunc='sum')
gender_min = df.pivot_table(values='rating', index='gender',aggfunc='min')
gender_max = df.pivot_table(values='rating', index='gender',aggfunc='max')
print(gender_mean2)
print(gender_sum)
print(gender_min)
print(gender_max)