import os
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


path2016 = "/Users/mainroot/RPC-test_data/last/2016/"
path2017 = "/Users/mainroot/RPC-test_data/last/2017/"
path2018 = "/Users/mainroot/RPC-test_data/last/2018/"

fileList2016 = os.listdir(path2016)
fileList2017 = os.listdir(path2017)
fileList2018 = os.listdir(path2018)


yDevAll2016 = pd.DataFrame()
yDevAll2017 = pd.DataFrame()
yDevAll2018 = pd.DataFrame()
yDevAll = pd.DataFrame()


for fileName in fileList2016:
    df = pd.read_csv(path2016 + fileName)
    for colName in ['Imon_change_date','lumi_start_date','lumi_end_date','uxc_change_date']:
        df[colName] = pd.to_datetime(df[colName])

    
    L = df["inst_lumi"]
    I = df["Imon"]

    lineFitter = linear_model.LinearRegression(fit_intercept=False)
    lineFitter.fit(L.values.reshape(-1, 1), I)
    IPredict = lineFitter.predict(L.values.reshape(-1, 1))
    coef1 = lineFitter.coef_

    x = df["Vmon"] / df["press"]
    y = (I - IPredict) / L
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, train_size=0.8, test_size=0.2)
    
    lineFitter = linear_model.LinearRegression()
    lineFitter.fit(xTrain.values.reshape(-1, 1), yTrain)
    yPredict = lineFitter.predict(xTest.values.reshape(-1, 1))
    coef2 = lineFitter.coef_
    intercept2 = lineFitter.intercept_

    ImonPredict = df["inst_lumi"] * (coef1 + coef2 * df["Vmon"] / df["press"] + intercept2)
    
    #plt.plot(df["Imon_change_date"], df["Imon"])
    #plt.plot(df["Imon_change_date"], lineFitter.predict(L.values.reshape(-1, 1)))
    plt.plot(df["inst_lumi"], df["Imon"], ".")
    plt.plot(df["inst_lumi"], ImonPredict, ".")
    plt.show()


