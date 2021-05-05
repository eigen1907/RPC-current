import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import mode


"""
path2017 = "/Users/mainroot/RPC_modified_data/golden/2017/"
fileList = os.listdir(path2017)

df = pd.read_csv(path2017 +  "dpid_3222_2017.csv")
for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
    df[colName] = pd.to_datetime(df[colName])

df = df[(df.Imon_change_date > pd.to_datetime("2017-09-26 11:00:00")) & (df.Imon_change_date < pd.to_datetime("2017-09-26 16:00:00"))]

plt.plot(df.Imon_change_date, df.Vmon, ".")
plt.show()
"""


# 2017의 경우
# dpid 315: 9월 26일 12:00 ~ 15:00 testing data 분포
# dpid 316: 9월 26일 12:00 ~ 16:00 testing data 분포
# 전체적으로 같으니 안정적이게 9월 26 11:00 ~ 16:00 데이터 버리기

# 2016의 경우
# Testing 값 없음

# 2018의 경우 6월 6일에서 10일 사이에 존재
# 안정적이게 6월 7일 06:00 ~ 6월 9일 06:00 데이터 버리기


"""
path2018 = "/Users/mainroot/RPC_modified_data/golden/2018/"
fileList = os.listdir(path2018)



for fileName in fileList:
    df = pd.read_csv(path2018 + fileName)
    for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
        df[colName] = pd.to_datetime(df[colName])


    plt.plot(df.Imon_change_date, df.Vmon, ".")
    plt.show()

"""


"""
df = pd.read_csv(path2018 + "dpid_2979_2018.csv")
print(df)


for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
    df[colName] = pd.to_datetime(df[colName])

df = df[(df.Imon_change_date > pd.to_datetime("2018-06-07 06:00:00")) & (df.Imon_change_date < pd.to_datetime("2018-06-09 06:00:00"))]

plt.plot(df.Imon_change_date, df.Vmon, ".")
plt.show()

"""


"""
path = "/Users/mainroot/RPC_modified_data/goldenNoTesting/2016/"
#path2 = "/Users/mainroot/RPC_modified_data/golden/2018/"
fileList = os.listdir(path)


for fileName in fileList:
    df = pd.read_csv(path + fileName)
    #df2 = pd.read_csv(path2 + fileName)
    for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
        df[colName] = pd.to_datetime(df[colName])
        #df2[colName] = pd.to_datetime(df2[colName])

    plt.plot(df.Imon_change_date, df.Vmon / df.press, ".")
    plt.show()

    #plt.plot(df2.Imon_change_date, df2.Vmon, ".")
    #plt.show()


#2016은 대략 9월 18일 이전과 이후로 나뉨. V 에 대한 formula가 바뀐거 같아 이걸로 나눠봅시다.
#2018은 7월 27일 부터 8월 19일 19:00:00까지 뚝 떨어지는 구간이 발생 그외에는 V / P 값이 크게 변하는 구간 안보임
"""



stdList = []
meanList = []
modeList = []


path = "/Users/mainroot/RPC_modified_data/goldenSep/2016First/"
fileList = os.listdir(path)

for fileName in fileList:
    df = pd.read_csv(path + fileName)
    for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
        df[colName] = pd.to_datetime(df[colName])


    meanOfIoverL = np.mean(df.Imon / df.inst_lumi)
    stdOfIoverL = np.std(df.Imon / df.inst_lumi)
    
    modeOfIoverL = mode(df.Imon / df.inst_lumi)
    


    stdList.append(stdOfIoverL)
    meanList.append(meanOfIoverL)


    modeList.append(modeOfIoverL[0][0])

    
    hist, bins = np.histogram(df.Imon/df.inst_lumi, 500, [0.0, 0.005])
    plt.figure(figsize=(12, 10))
    plt.hist(df.Imon/df.inst_lumi, 500, [0.0, 0.005], color="r")
    plt.xlim(0, 0.005)
    plt.title(f"Mean: {meanOfIoverL} \n Std: {stdOfIoverL}, \n Mode: {modeOfIoverL[0][0]}")
    plt.show()


"""
newMeanList = list(filter(np.isfinite, meanList))
newModeList = list(filter(np.isfinite, modeList))


ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)
ax1.set_xlabel("STD of I/L")
ax2.set_xlabel("Mean of I/L")
ax3.set_xlabel("mode of I/L")
ax1.hist(stdList, bins=50)
ax2.hist(newMeanList, bins=50)
ax3.hist(newModeList, bins=50)
plt.suptitle("value of all dpid, histogram")
plt.tight_layout()
plt.show()
"""


"""
path = "/Users/mainroot/RPC_modified_data/goldenSep/2016First/"
fileList = os.listdir(path)

for fileName in fileList:
    df = pd.read_csv(path + fileName)
    for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
        df[colName] = pd.to_datetime(df[colName])

    PTCorrection =  df.Vmon / (df.press / (df.temp + 273) * 293 / 965)

    plt.plot(df.Imon_change_date, PTCorrection, ".")
    plt.show()
"""