import tensorflow as tf
import numpy as np
import pandas as pd

# 위의 데이터를 넣어 테스트를 해 보도록 합시다.
# 사용자로부터 키와 몸무게를 입력받아 마른정도(thin,normal,fat)을 출력하는 웹어플리케이션을 작성합니다.

csv = pd.read_csv("../Data/bmi.csv")
# print(csv)
'''       height  weight   label
0         142      62     fat
1         142      73     fat
2         177      61  normal
3         187      48    thin'''

# 학습시키기 위하여 label의 종류 3가지를 (fat, normal,thin) one-hotEncoding

print(csv['height'].max(),csv['height'].min())   #200 120
print(csv['weight'].max(),csv['weight'].min())   #80 35

#키와 몸무게 기본값들이 170,57등 값의 부피가 크므로
# 평균정규화 ( 값의 범위를 0~1 사이값으로 줄인다)
csv['height'] = csv['height'] / 200          #키의 최대값이 200
csv['weight'] = csv['weight'] / 100          #몸무게가 최대값이 80을 넘지 않기 때문

# print(csv['height'].max(),csv['height'].min())   #1.0    0.6
# print(csv['weight'].max(),csv['weight'].min())   #0.8    0.35

#답의 종류를 직접 0, 1로 바꾼다
bclass = {"thin":[1,0,0],"normal":[0,1,0],"fat":[0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))

# Pandas에서 제공하지 않는 기능을 추가하는 방법은 apply()를 쓰거나 pure python code로 감싸는 방법이 있다.
# apply는 function을 parameter로 넣을 수 있는데 이 function에 pandas가 제공하지 않는 기능을 만들어서 넣으면 된다.
# 여기서 np.array(bclass[x]) 는 앞의 csv['label']값이 람다식에 x값에 들어가서 나온 값이 label_pat에 넣어준다.
# csv['label']값에 람다식을 적용시킨다.

#테스트를 위한 데이터 분류
test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])
'''
test_ans:  [array([0, 0, 1]), array([1, 0, 0]), 
'''

#데이터 플로우 그래프 구출하기
#플레이스 홀더 선언하기

x = tf.placeholder(tf.float32,[None,2])   #키와 몸무게 데이타 넣기
y_ = tf.placeholder(tf.float32,[None,3])   #정답 레이블 넣기

#변수 선언하기  0으로 채운다.
W = tf.Variable(tf.zeros([2,3]))      #가중치      2:피쳐수 3:답의 수
b = tf.Variable(tf.zeros([3]))        #bias     기준치      3:답의 수

# 소프트맥스 회귀 정의하기 (자동으로 가중치와 기준치를 만든다.)
y = tf.nn.softmax(tf.matmul(x, W) +b )

#모델 훈련하기
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cross_entropy)

#정답 구하기
predict = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(predict,tf.float32))

#세션 시작하기
sess = tf.Session()
sess.run(tf.global_variables_initializer()) #변수 초기화

#학습시키기
# W 와 b를 알고자 하는 것이 목적
# 각 feature 마다 가중치가 얼마인지, 각 feature 마다 bias는 얼마인지
for step in range(3500):
    i = (step * 100) %14000
    rows = csv[1 + i : 1 + i +100]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x:x_pat, y_:y_ans}
    sess.run(train,feed_dict=fd)
    if step % 500 ==0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x:test_pat,y_:test_ans})
        # print("step=",step,"cre=",cre,"acc=",acc)

# 최종적인 정답률 구하기
# acc = sess.run(accuracy, feed_dict={x:test_pat,y_:test_ans})
# print("정답률=",acc)

# 최종적인 정답률 구하기
print(sess.run(W))
print(sess.run(b))

k = np.array([[46/100,174/200]])

y1 = tf.nn.softmax(tf.matmul(x, sess.run(W)) +sess.run(b) )
print(sess.run(y1,feed_dict={x:k}))

acc = sess.run(accuracy, feed_dict={x:test_pat,y_:test_ans})
print("정답률=",acc)