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

def getPrecision(predicted,real): #lists
    prediction = precision_score(real, predicted)
    return prediction
    
def predictRegression(day):
    try:
        regression = joblib.load('regressionModel.pkl')
    except:
        return -1 #error
    ordd = dt.datetime.strptime(day,"%d-%m-%Y").date().toordinal()
    prediction = regression.predict(ordd)
    return prediction