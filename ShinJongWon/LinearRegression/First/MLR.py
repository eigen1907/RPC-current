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
    
    
    X = df[["inst_lumi", "Vmon", "press"]]
    y = df[["Imon"]]

    XTrain, XTest, yTrain, yTest = train_test_split(X, y, train_size=0.8, test_size=0.2) 

    lineFitter = linear_model.LinearRegression()
    lineFitter.fit(X, y)
    IPredict = lineFitter.predict(X)
    coef1 = lineFitter.coef_
    intercept1 = lineFitter.intercept_

    plt.plot(df["Imon_change_date"], df["Imon"])
    plt.plot(df["Imon_change_date"], IPredict)
    plt.show()