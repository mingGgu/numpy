import tensorflow as tf

a = tf.placeholder(tf.int32,[3])

# 위에서 만든 placeHolder가 사용되는 수식(Data Flow)을 만들어 봅시다.
b = tf.constant(2)
x_op = a * b

# 위의 수식을 실행시켜 봅시다.
# tensor의 Session을 얻어온다.
sess = tf.Session()

# 위의 수식을 실행시키려고한다. a에는 결정되지 않은 값(placeHoler)를 가지고있기때문에
# 실행시에 반드시 placeHoler에 값을 설정 해 줘야한다.
# 설정 함수가 feed_dic 이다. placeHolder가 여러개일 수 있기때문에
# 어떤 변수에 값을 지정할 것인지 변수명을 적어주고 같은 type을 넣어준다.
# 여기선 배열이기때문에 a[1,2,3] 이라고 적어준것
r1 = sess.run(x_op, feed_dict={a:[1,2,3]})
print(r1)
'''
[2 4 6]
'''

r2 = sess.run(x_op, feed_dict={a:[4,5,6]})
print(r2)
'''
[ 8 10 12]
'''

