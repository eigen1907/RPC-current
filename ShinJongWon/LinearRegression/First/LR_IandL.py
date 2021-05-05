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


coef2017 = []
intercept2017 = []

for fileName in fileList2017:
    df = pd.read_csv(path2017 + fileName)
    for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
        df[colName] = pd.to_datetime(df[colName])
    x = df.press.values.reshape(-1, 1)
    y = df.Vmon
    lineFitter = LinearRegression()
    lineFitter.fit(x, y)
    yPredict = lineFitter.predict(x)


    coef2017.append(lineFitter.coef_)
    intercept2017.append(lineFitter.intercept_)

    plt.plot(df.press, df.Vmon, ".")
    plt.plot(df.press, yPredict, ".")
    plt.title(f"coef: {lineFitter.coef_}, intercept: {lineFitter.intercept_}")
    plt.show()



"""
plt.hist(coef2016, bins=50)
plt.show()

plt.hist(intercept2016)
plt.show()
"""
"""
for fileName in fileList2017:
    df = pd.read_csv(path2017 + fileName)
    x = df[["inst_lumi"]]
    y = df[["Imon"]]
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, train_size=0.8, test_size=0.2)
    lineFitter = LinearRegression()
    lineFitter.fit(xTrain, yTrain)
    yPredict = lineFitter.predict(xTest)
    yDev = yPredict - yTest
    yDevAll2017 = pd.concat([yDevAll2017, yDev], axis=0)

for fileName in fileList2018:
    df = pd.read_csv(path2018 + fileName)
    x = df[["inst_lumi"]]
    y = df[["Imon"]]
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, train_size=0.8, test_size=0.2)
    lineFitter = LinearRegression()
    lineFitter.fit(xTrain, yTrain)
    yPredict = lineFitter.predict(xTest)
    yDev = yPredict - yTest
    yDevAll2018 = pd.concat([yDevAll2018, yDev], axis=0)
"""
"""
print("="*80)
print("2016 Data")
print("Entries: ", len(yDevAll2016))
print("Mean: ", np.mean(yDevAll2016.Imon))
print("RMS: ", np.sqrt(np.mean(yDevAll2016.Imon**2)))
plt.hist(yDevAll2016, bins=500)
plt.xlim(-5, 5)
plt.show()



print("="*80)
print("2017 Data")
print("Entries: ", len(yDevAll2017))
print("Mean: ", np.mean(yDevAll2017.Imon))
print("RMS: ", np.sqrt(np.mean(yDevAll2017.Imon**2)))
plt.hist(yDevAll2017, bins=500)
plt.xlim(-5, 5)
plt.show()

print("="*80)
print("2018 Data")
print("Entries: ", len(yDevAll2018))
print("Mean: ", np.mean(yDevAll2018.Imon))
print("RMS: ", np.sqrt(np.mean(yDevAll2018.Imon**2)))
plt.hist(yDevAll2018, bins=500)
plt.xlim(-5, 5)
plt.show()


yDevAll = pd.concat([yDevAll2016, yDevAll2017, yDevAll2018], axis=0)
print("="*80)
print("All Data")
print("Entries: ", len(yDevAll))
print("Mean: ", np.mean(yDevAll.Imon))
print("RMS: ", np.sqrt(np.mean(yDevAll.Imon**2)))
plt.hist(yDevAll, bins=500)
plt.xlim(-5, 5)
plt.show()
print("="*80)
"""

