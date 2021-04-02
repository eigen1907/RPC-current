import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
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
    L = df["inst_lumi"]
    I = df["Imon"]

    lineFitter = LinearRegression(fit_intercept=False)
    lineFitter.fit(L.values.reshape(-1, 1), I)
    IPredict = lineFitter.predict(L.values.reshape(-1, 1))

    x = df["Vmon"] / df["press"] * 1e6
    y = (I - IPredict) / L * 1e6
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, train_size=0.8, test_size=0.2)

    lineFitter = LinearRegression()
    lineFitter.fit(xTrain.values.reshape(-1, 1), yTrain)
    yPredict = lineFitter.predict(xTest.values.reshape(-1, 1))

    
    yDev = yTest - yPredict
    yDev /= 1e6
    yDevAll2016 = pd.concat([yDevAll2016, yDev], axis=0)

    



"""
print("="*80)
print("2016 Data")
print(yDevAll2016.info())
print("Entries: ", len(yDevAll2016))
print("Mean: ", np.mean(yDevAll2016))
print("RMS: ", np.sqrt(np.mean(yDevAll2016**2)))
print("="*80)
print(yDevAll2016)
plt.hist(yDevAll2016, bins=500)
plt.xlim(-0.1, 0.1)
plt.show()
"""

"""


df = pd.read_csv("/Users/mainroot/RPC-test_data/last/2016/dpid_319_2016.csv")
L = df["inst_lumi"]
I = df["Imon"]

lineFitter = LinearRegression()
lineFitter.fit(L.values.reshape(-1, 1), I)
IPredict = lineFitter.predict(L.values.reshape(-1, 1))

x = df["Vmon"] / df["press"] * 1e6
y = (I - IPredict) / L * 1e6

print(x)
print("="*80)
print(y)
print("="*80)


xTrain, xTest, yTrain, yTest = train_test_split(x, y, train_size=0.8, test_size=0.2)

lineFitter = LinearRegression()
lineFitter.fit(xTrain.values.reshape(-1, 1), yTrain)
yPredict = lineFitter.predict(xTest.values.reshape(-1, 1))

yDev = yTest - yPredict
print(yDev)
"""
