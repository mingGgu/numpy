import pandas as pd
import numpy as np
import tensorflow as tf

csv = pd.read_csv("../Data/bmi.csv")

print(csv.head())

#    height  weight   label
# 0     142      62     fat
# 1     142      73     fat
# 2     177      61  normal
# 3     187      48    thin
# 4     153      60     fat


#이파일에는 사람들의 키, 몸무게, 마른정도
#       마른정도의 값은 fat, normal, thin
#       즉 정답(Label)의 수는 3가지 입니다.


# 1. 이것을 학습시키기 위해여
#           Label의 종류 3가지를 one-hot Encoding 하여야 합니다.

# 2.

#제일키가 큰키와 제일작은키는 얼마인가요?
print(csv['height'].max(), csv['height'].min()  )       #200 120

#제일큰몸무게와 제일작은 몸무게는 얼마인가요?
print(csv['weight'].max(), csv['weight'].min()  )       #80 35


#기계학습 시키기위한 feature들의 값의 범위가 너무커서
#이것들의 범위를 0~1사이의 값으로 줄이고 싶어요        ==> 정규화

# 키의 제일큰값이 200을 넘지 않아요  그래서 200으로 나누고
# 몸무게의 제일큰값은 100을 넘지 않아요 그래요 100으로 나누려고 합니다.

csv['height'] = csv['height'] / 200
csv['weight'] = csv['weight'] / 100

#제일키가 큰키와 제일작은키는 얼마인가요?
print(csv['height'].max(), csv['height'].min()  )       #1.0 0.6

#제일큰몸무게와 제일작은 몸무게는 얼마인가요?
print(csv['weight'].max(), csv['weight'].min()  )       #0.8 0.35

#값의 범위를 축소시켜 0~1사이의 값들로 만들었습니다.


#답의 종류에 따른 one-hot 인코딩 값을 정해요.
bclass = {"thin":[1,0,0], "normal":[0,1,0],"fat":[0,0,1]}


# 그럼, 위에서 계획한 한데로
# 원본데이터의 label에 따라 one-hot 인코딩 테이블을 생성하여
# 새로운 칼럼(label_pat)를 추가 해 봅시다.

csv['label_pat'] = csv["label"].apply(lambda x: np.array(bclass[x]))


print(csv.head())

#  height  weight   label  label_pat
# 0   0.710    0.62     fat  [0, 0, 1]
# 1   0.710    0.73     fat  [0, 0, 1]
# 2   0.885    0.61  normal  [0, 1, 0]
# 3   0.935    0.48    thin  [1, 0, 0]
# 4   0.765    0.60     fat  [0, 0, 1]


# 갖고있는 데이터를 모두 훈련에 참여시키면
# 훈련된 데이타만 잘 알아 맞추어요.
#  즉 새로운 데이터에 대해서는 잘 못 알아맞춰요
#       ==> overfit
#  기준이 애매해요..
#   반드시는 아니고 보통은 갖고 데이터의 70~80%를 훈련에 참여시키고
#   나머지 데이터를 갖고 반드시 검증을 해야 합니다.


print(csv.tail())
#
#        height  weight   label  label_pat
# 19995   0.610    0.58     fat  [0, 0, 1]
# 19996   0.965    0.69  normal  [0, 1, 0]
# 19997   0.965    0.37    thin  [1, 0, 0]
# 19998   0.975    0.51    thin  [1, 0, 0]
# 19999   0.815    0.67  normal  [0, 1, 0]

#전체 데이터의수는 20000건이 있어요
#이중에 3분의 2를 훈련데이터로 3분의 1을 검증데이터로 사용하려고 해요.


#15000번째 인덱스부터 20000번째까지의 데이터를 뽑아 검증데이터로 담아요
test_csv = csv[15000:20000]

#검증을 위한 데이터 test_csv로 부터 문제와 답을 나누어요
test_pat = test_csv[['weight','height']]
# test_ans = test_csv['label_pat']
# print(type(test_ans))   #<class 'pandas.core.series.Series'>
#       test_csv['label_pat']가 Series라서 list로 형변환 해야 합니다.
test_ans = list(test_csv['label_pat'])


print(test_pat.head())
print(test_ans[:5])

#        weight  height
# 15000    0.55   0.690
# 15001    0.36   0.760
# 15002    0.72   0.915
# 15003    0.51   0.990
# 15004    0.47   0.745
# [array([0, 0, 1]), array([1, 0, 0]), array([0, 1, 0]), array([1, 0, 0]), array([0, 1, 0])]


#훈련시키기 위한 문제 placeHolder를 만들어요
x = tf.placeholder(tf.float32, [None,2])

#훈련시키기 위한 답 placeHolder를 만들어요
y_ = tf.placeholder(tf.float32, [None,3])


#가중치를 위한 배열을 만들어요
#       [feature의 수, 답의 수]
W = tf.Variable(tf.zeros([2,3]))


# bias(편향)는 만들어요
# 바이어스의 값의 수는 답의 수와 동일하게 해요
# 답의수 3가지 입니다. thin, normal, fat
# 각각의 feature에 각각 weight을 적용한 값이 thin이 되려면 얼마(?) 넘어야 해요
# 각각의 feature에 각각 weight을 적용한 값이 normal이 되려면 얼마(?) 넘어야 해요
# 각각의 feature에 각각 weight을 적용한 값이 fat이 되려면 얼마(?) 넘어야 해요
#   각각에 대한 기준치(임계치)가 3개의값이 필요해요
#   일단 0으로 채워두면 tensor을 학습을 하면서 이것을 알맞은 값을 셋팅을 합니다.
b = tf.Variable(tf.zeros([3]))


#텐서가 제공하는 기계학습을 위한 softmax객체를 생성해요
#       (모델을 만들어요)
                  # y = wx + b
                  # y = w1x1 + w2x2 + b1 + b2 + b3
y = tf.nn.softmax( tf.matmul(x,W)+b)                            #C


#훈련된 결과와 진짜답과의 거리를 가능하면 작게 만들기 위한
#객체를 생성해요

#진짜답과 예측한 답의 합을 담아요(잔차의 합)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))                   #B

#그 잔차의 합의 최소화 되게끔 해주는 개체를 생성해요.
optimizer= tf.train.GradientDescentOptimizer(0.01)

#optimzer 객체를 통해 train객체를 생성해요.
#optimer 객체를 통해 훈련시키고 싶어요
train = optimizer.minimize(cross_entropy)                       #A
# 이 train객체를 텐서를 이용하여 실행시킬텐데
# 이 수식에는 placeHolder가 몇개 있나요??
# A의 수식에 사용된 cross_entropy는 B이며
#   B의 cross_entropy는 y_와 y를 포함한다.
#   y_ 는 진짜답을 답을 placeHolder이며
#   y  훈련을 위한 식이며 즉 훈련된 결과가 담길 변수이다.
#           이식에 문제가 담길 placeHolder x가 포함된다.
#   그래서 tensor에서 실행시길때
#           y_와 x에 해당하는 값을 설정해야 합니다.



#훈련시키는 과정에서 정확도를 확인하기 위한 수식을 만들어요

#예측한 답과 진짜답을 비교하여 predict배열에 담아요
predict = tf.equal( tf.argmax(y,1), tf.argmax(y_,1))

#예측한 답과 진짭을 비교한 predict는 boolean 배열인데
#이것을 실수형으로 변환하여 평균값을 얻어요
accuracy = tf.reduce_mean( tf.cast( predict, tf.float32  ) )


sess = tf.Session()
sess.run(tf.global_variables_initializer())


# 원본데이터 20000개 중에
# 검증용 데이터 15000~20000를 제외한
# 모든 데이터를 훈련시키려고 해요

# 15000개를 한꺼번에 훈련시키기 않고
#   100개씩 끊어서 훈련시키려고 해요.

# w와 b를 알고자 하는 것이 목적
#  각 feature마다 가중치가 얼마인지
#  각 feature마다 bias는 얼마인지
for step in range(3500):
    i = (step*100) % 14000
    # i는 0, 100, 200 ~  14900

    #i번째 부터 100개씩 뽑아와요
    rows = csv[i+1:i+1+100]

    #문제와 답을 분리해요
    x_pat = rows[['weight','height']]
    y_ans = list(rows['label_pat'])

    #훈련객체 train에 사용된 placeHolder에 적용할 객체를 만들어오
    fd = {x:x_pat,y_:y_ans}

    sess.run(train,feed_dict=fd)

    if step % 500 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x:test_pat, y_:test_ans})
        print("step=:",step, "cre:",cre, "acc:",acc)


# for step in range(0,14900, 100):
#     print(step)

acc = sess.run(accuracy, feed_dict={x:test_pat, y_:test_ans})
print("최종정답률:",acc)

#위의 학습결과를 적용해 봅시다

#위의 학습결과로 부터 학습된 W와 b를 변수에 담아요
w1 = sess.run(W)
b1 = sess.run(b)
# print(w1)

#알고자 하는 사람의 몸무게와 키를 다음과 같이 정규화시켜요
#학습한 x가 0~1사이의 범위이므로 알고자 하는 데이터도 같게 만들어요
x1 = np.array([[53/100,136/200]],np.float32)

#알고자 하는 식을 만들어요
#y = wx + b
#w와 b에는 각각 학습된 최적의 w와 b를 적용해요
#행렬곱을 위하여 텐서의 matmul함수를 이용해요.
y1 = tf.matmul(x1,w1)+b1

#예측한 결과 y1을 one-hot 인코딩으로 만들어
#어디에 불이 들어왔는지를 갖고 와요
#thin이면 0번째 불이 들어와요 1 0 0   ==> 0을 반환해요
#normal이면 1번째 불이들어요 0 1 0   ==> 1을 반환해요
#fat이면 2번째 불이들어와요.  0 0 1   ==> 2륿 반환해요
predict1 = tf.argmax(y1,1)

print(sess.run(predict1))

sess.close()

#  bclass = {"thin":[1,0,0], "normal":[0,1,0],"fat":[0,0,1]}
# 189,79,normal

# 174,46,thin
#1) 위의 데이터를 넣어 테스트 해 보도록 합니다.
#2) 사용자로 부터 키와 몸무게를 입력받아 마른정도(thin, normal, fat)를 출력하는
#           웹어플리케이션을 작성합니다.


#
# 167,65,normal     010     1
# 146,53,normal     010     1
# 174,69,normal     010     1
# 173,35,thin       100     0
# 136,53,fat        001     2
# 189,79,normal     010     1
# 139,78,fat        001     2
# 121,72,fat        001     2
# 120,63,fat        001     2