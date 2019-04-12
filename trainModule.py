import numpy as np
import pandas as pd
from sklearn import linear_model,model_selection

def onehotTrain(testdata):

    names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
             'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']
    data = pd.read_csv('../Data/adult.data.txt',header=None, names=names)
    data = data[['age','workclass','education','sex','race','hours-per-week','occupation','income']]
    new_df = pd.get_dummies(data)
    x1 = new_df.iloc[:,:-2]
    y1 = new_df.iloc[:,-1]
    train_x, test_x, train_y, test_y = model_selection.train_test_split(x1,y1)
    lr = linear_model.LogisticRegression()
    lr.fit(train_x,train_y)
    test = [testdata]
    test_df = pd.DataFrame(test, columns=['age','workclass','education','sex','race','hours-per-week','occupation'])
    data2 = data.append(test_df)
    one_hot_data2 = pd.get_dummies(data2)

    print(len(one_hot_data2.columns))
    print(len(new_df.columns))
    # 맨 마지막이 내가 알고싶은 데이터니까 -1, 맨뒤에 2개 income은 빼줘야하니까 -2(맨마지막 2개)
    pre_x = np.array(one_hot_data2.iloc[-1,:-2]).reshape(1,-1)
    pre_y = lr.predict(pre_x)

    return pre_y

