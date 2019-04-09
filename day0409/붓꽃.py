from sklearn import datasets, svm, neighbors, model_selection
import numpy as np
import pandas as pd

# 사이킷런의 dataset이 제공하는 iris데이터를 읽어와 봅시다
iris = datasets.load_iris()

# iris의 정체를 확인하고 문제(꽃받침의 길이, 넓이, 꽃잎의 길이, 넓이)와 답(품종)이 어떤 속성으로 제공되는지 확인 해 봅시다.
# print(iris)
# print(iris['DESCR'])
# print(iris['data'])
# print(iris['target'])
# print(iris['target_names'])

# 골고루 잘 섞어서 문제와 답을 분리하여 훈련용데이터 테스트용데이터로 분리해 봅시다
# 문제와 답을 주면 훈련용과 테스터용 두 개로 나눠준다.
train_x , test_x, train_y, test_y = model_selection.train_test_split(iris['data'], iris['target'])
# print(train_x)
# print(test_x)
# print(train_y)
# print(test_y)

# r = knn.predict(test_x)
# print(np.mean(r==test_y))
# print(test_x)
# print(test_x)

knn = neighbors.KNeighborsClassifier()
knn.fit(train_x, test_y)

label = iris['target_names']
x = [[4.6,3.6,1.,0.2]]
r = knn.predict(x)
result = label[r]
print(result)

