import tensorflow as tf
import numpy as np
import pandas as pd

student = [
            ['박민서',80,90,100],
            ['김경희',78,100,100],
            ['이혜민',89,99,99],
            ['도경수',77,95,10],
            ['디오쨩',28,53,61]
    ]

# placeHolder를 이용하여 각 학생의 평균을 구하여 출력해 봅니다.
student_score = tf.placeholder(tf.int32,[3])
student_jumsu = student.slice[1:4]
print(student_jumsu)
# avg = tf.constant(3)
# sum = student_score
