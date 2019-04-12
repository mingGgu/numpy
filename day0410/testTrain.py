# 연습) 고객의 나이, 직업분류, 학력, 직업,성별,인종,주당근무시간을 입력받아 연봉이 5만달러 이상이면 대출가능
# 그렇지 않으면 대출불가능을 출력하는 웹어플리케이션을 구현합니다.
# 단 직업분류, 학력, 직업,성별,인종은 우리가 훈련시킬 데이터 adult.data.txt의 내용으로 제한하도록 합니다.`

import numpy as np
import pandas as pd
from flask import Flask,render_template,request
import trainModule
app = Flask(__name__)

@app.route('/onehote',methods=['POST','GET'])
def onehotGet():
    names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
             'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
             'income']
    data = pd.read_csv('../Data/adult.data.txt',header=None, names=names)
    data = data[['age', 'workclass', 'education', 'sex', 'race', 'hours-per-week', 'occupation','income']]
    w = data['workclass'].unique()
    e = data['education'].unique()
    o = data['occupation'].unique()
    ra = data['race'].unique()
    s = data['sex'].unique()

    result=''

    if request.method == 'POST':
        r = []
        age = request.form['age']
        workclass = request.form['workclass']
        education = request.form['education']
        sex = request.form['sex']
        race = request.form['race']
        hoursperweek = request.form['hoursperweek']
        occupation = request.form['occupation']
        r.append(int(age))
        r.append(workclass)
        r.append(education)
        r.append(sex)
        r.append(race)
        r.append(int(hoursperweek))
        r.append(occupation)
        print(r)
        resul = trainModule.onehotTrain(r)

        result = '대출 불가능'
        if resul == 1:
            result = '대출가능'

    return render_template('onehot.html',result=result,ra=ra,w=w,e=e,o=o,s=s)

if __name__ == '__main__':
    app.run(debug=True, host='203.236.209.100')