import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import multiprocessing
from itertools import compress



def is_outlier(points, thresh=3.5):
    points = np.array(points)
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh



def getML_V1_Param(rpcImonSepPath, dpidName):

    rpcImonData = pd.read_csv(rpcImonSepPath + dpidName, low_memory=False)

    rpcImonData["Imon_change_date"] = pd.to_datetime(rpcImonData["Imon_change_date"], format='%Y-%m-%d %H:%M:%S', errors="raise")


    x1 = rpcImonData["inst_lumi"]
    x2 = rpcImonData["Vmon"]
    x3 = rpcImonData["temp"]
    x4 = rpcImonData["inst_lumi"] * np.exp(rpcImonData["Vmon"] / rpcImonData["press"])
    x5 = rpcImonData["relative_humodity"]
    x6 = rpcImonData["press"]
    x7 = (rpcImonData["Imon_change_date"] - rpcImonData["Imon_change_date"][0]).astype(int) / 10**9

    X = pd.concat([x1, x2, x3, x4, x5, x6, x7], ignore_index=True, axis=1)
    y = rpcImonData["Imon"]

    lineFitter = LinearRegression()
    lineFitter.fit(X, y)

    yPredict = lineFitter.predict(X)

    paramDf = pd.DataFrame([[
        lineFitter.intercept_,
        lineFitter.coef_[0],
        lineFitter.coef_[1],
        lineFitter.coef_[2],
        lineFitter.coef_[3],
        lineFitter.coef_[4],
        lineFitter.coef_[5],
        lineFitter.coef_[6]]
    ], columns=["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7"])

    return paramDf


if __name__ == "__main__":
    rpc2016former = os.listdir("/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/2016_former/")
    rpc2016latter = os.listdir("/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/2016_latter/")
    rpc2017 = os.listdir("/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/2017/")
    rpc2018dropping = os.listdir("/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/2018_dropping/")
    rpc2018normal = os.listdir("/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/2018_normal/")


    for i in range(len(rpc2016former)):
        rpc2016former[i] = rpc2016former[i][0:-9]

    for i in range(len(rpc2016latter)):
        rpc2016latter[i] = rpc2016latter[i][0:-9]

    for i in range(len(rpc2017)):
        rpc2017[i] = rpc2017[i][0:-9]

    for i in range(len(rpc2018dropping)):
        rpc2018dropping[i] = rpc2018dropping[i][0:-9]

    for i in range(len(rpc2018normal)):
        rpc2018normal[i] = rpc2018normal[i][0:-9]

    sharedDpids = list(set(rpc2016former) & set(rpc2016latter) & set(rpc2017) & set(rpc2018dropping) & set(rpc2018normal))

    columnList = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7"]
    paramList = [pd.DataFrame(columns=columnList) for i in range(5)]

    rpcImonPath = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/"
    rpcImonSepFolders = os.listdir(rpcImonPath)
    rpcImonSepFolders.sort()

    rpcImonSepPaths = []

    for i in range(len(rpcImonSepFolders)):
        rpcImonSepPaths.append(rpcImonPath + rpcImonSepFolders[i] + "/")
        eachDpids = []
        for j in range(len(sharedDpids)):
            eachDpids.append(sharedDpids[j] + "_" + rpcImonSepFolders[i][0:4] + ".csv")

        for eachDpid in eachDpids:
            paramList[i] = paramList[i].append(getML_V1_Param(rpcImonSepPaths[i], eachDpid), ignore_index=True)


    print(len(paramList))
    print(len(paramList[0]))