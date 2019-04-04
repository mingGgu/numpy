from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc, colors

app = Flask(__name__)
@app.route('/name',methods=['GET','POST'])
def socreGet():
    fname=''
    name = ''
    if request.method == 'POST':
        print('post방식 요청')
        rc('font', family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/NanumBarunGothicUltraLight.ttf').get_name())
        score = pd.read_csv('Data/scores.csv')
        score.index = score['name']
        del score['name']

        name = request.form['name']
        x = ['kor', 'eng', 'mat', 'bio']
        plt.bar(range(len(x)),score.loc[name][x],0.6,color='pink')
        plt.title(name+'의 과목별 점수')
        plt.xticks(range(len(x)),x)
        fname = 'static/'+name+'.png'
        plt.savefig(fname)
        plt.close()

    return render_template('score.html', name=name, fname=fname)

if __name__ == '__main__':
    app.run(host='203.236.209.100',debug=True)

