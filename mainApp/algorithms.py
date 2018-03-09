from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
import numpy as np
import datetime as dt

def makeRegression(usage, days):
    ordd = []
    for d in days:
        ordd.append(dt.datetime.strptime(d,"%d-%m-%Y").date().toordinal())
    regression = LinearRegression()
    regression.fit(np.transpose(np.matrix(ordd)), np.transpose(np.matrix(usage)))
    joblib.dump(regression, 'regressionModel.pkl')
    
def predictRegression(day):
    regression = joblib.load('regressionModel.pkl')
    ordd = dt.datetime.strptime(day,"%d-%m-%Y").date().toordinal()
    prediction = regression.predict(x_predict)
    return prediction