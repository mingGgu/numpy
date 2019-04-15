import tensorflow as tf

# 크기가 정해지지 않은 1차원 배열의 placeHolder를 만든다.
# 1차원이라 [None]/ 2차원은 [[None]] / 10행의 어떤크기의 열은 [10][None] 이된다.
arr = tf.placeholder(tf.int32,[None])

# 곱해줄 값을 상수로 만드는 것이 좋다.
a = tf.constant(2)

#  arr * a 한 수식을 만든다.
result = arr * a

# tensor의 Session을 얻어 위의 수식을 실행시킨다.
# 실행시킬때는 placeHolder의 값을 지정해준다.
sess = tf.Session()
r1 = sess.run(result, feed_dict={arr:[1,2]})
r2 = sess.run(result, feed_dict={arr:[10,20,30,40]})
x = [7,8,9]
r3 = sess.run(result, feed_dict={arr:x})
print(r1)
'''
[2 4]
'''
print(r2)

'''
[20 40 60 80]
'''

print(r3)
'''
[14 16 18]
'''
