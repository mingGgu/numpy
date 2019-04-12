import tensorflow as tf

# 텐서에서 사용할 상수 선언하기
a = tf.constant(2) #a는 2이외의 다른값을 가질수 없다는 뜻
b = tf.constant(3)
c = tf.constant(4)

calc1_op = a + b * c
print(calc1_op)
'''
Tensor("add:0", shape=(), dtype=int32)
# 텐서의 상수나 변수 수식의 결과를 바로 알아볼 수 없다.
  텐서의 실행환경에서 실행시키고 그 결과를 확인 할 수있다.
'''
calc2_op = (a+b) * c

sess = tf.Session()
r1 = sess.run(calc1_op)
r2 = sess.run(calc2_op)
print(r1)
print(r2)
'''
14
20
# 텐서의 스테이지를 열어서 결과를 확인 할 수있다.
'''

