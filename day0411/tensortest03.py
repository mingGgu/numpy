import tensorflow as tf

# tensorflow에서 사용할 상수(변하지 않는값)을 선언
# a는 120이외의 다른값을 가질 수 없어요
# java문법  =>  final int a = 120 이라고 사용
# 기본적으로 name='변수명' 까지 쓰는게 맞지만 생략가능
a = tf.constant(120, name='a')
b = tf.constant(130, name='b')
c = tf.constant(140, name='c')

# tensor에서 사용할 변수를 선언
v = tf.Variable(0,name='v')

# 실행되는 흐름(계산식의 흐름)을 그래프라고 한다.
calc_op = a + b + c
'''
# 위의 수식을 위해서는 몇번의 연산이 일어나나요
a 
 +  =  r 
b       +  =  calc_op
       c
       
# a + b + c 는 2번의 그래프(연산)을 가진다.
  수식을 만드는 것을 '데이터 플로우 그래프' 라고 합니다.
'''
# 위의 수식의 결과(calc_op)를 텐서변수 v에 대입한다.
# 계산속도가 빠르다.
# 아직은 계산되지 않은것.
# 실제 계산은 Tensor의 session을 얻고 그 session이 run을 만나야 계산된다.

# v에 수식을 담은 calc_op를 대입시킨다.
assign_op = tf.assign(v, calc_op)

# 텐서수식(assing_op)를 실행시키기 위해 session이 필요하다.
sess = tf.Session()

# 연산한 결과를 텐서변수 v에 담는다.
print(sess.run(assign_op))
print(assign_op)
'''
390
Tensor("Assign:0", shape=(), dtype=int32_ref)
'''

# v에 담긴 내용을 실행하여 출력한다.
print(sess.run(v))
print(v)
'''
390
<tf.Variable 'v:0' shape=() dtype=int32_ref>
'''
