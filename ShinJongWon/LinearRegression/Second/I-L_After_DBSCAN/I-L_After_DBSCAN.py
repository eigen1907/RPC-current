import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import multiprocessing
from sklearn.cluster import DBSCAN


### Regression Condition: inst_lumi => All Data, intercept => True
def plotFunction(rpcImonPath, plotPath, dpidName):
    rpcImonData = pd.read_csv(rpcImonPath + dpidName, low_memory=False)
    rpcImonData = rpcImonData.drop(columns=['lumi_start_date', 'lumi_end_date', 'uxc_change_date', 'dew_point', 'relative_humodity'])
    rpcImonData["Imon_change_date"] = pd.to_datetime(rpcImonData["Imon_change_date"])
    rpcImonData = pd.read_csv(rpcImonPath + dpidName, low_memory=False)
    
    rpcImonData.Imon_change_date = pd.to_datetime(rpcImonData.Imon_change_date)
    
    #### delete outlier as DBSCAN
    x1 = rpcImonData["Imon"]
    x1Max = max(x1)

    x2 = rpcImonData["inst_lumi"]
    x2Max = max(x2)

    x1Norm = x1 / x1Max
    x2Norm = x2 / x2Max

    X = pd.concat([x1Norm, x2Norm], ignore_index=True, axis=1)
    model = DBSCAN(eps=0.08, min_samples=50)
    model_labels = model.fit_predict(X)

    #### label = 0 => normal, label != 0 => outlier
    rpcImonData["label"] = model_labels


    #### Linear Regression I-L
    x = rpcImonData[rpcImonData["label"] == 0].inst_lumi.values.reshape(-1, 1)
    y = rpcImonData[rpcImonData["label"] == 0].Imon
    
    lineFitter = LinearRegression()
    if len(x) == 0:
        return

    lineFitter.fit(x, y)

    yPredict = lineFitter.predict(rpcImonData.inst_lumi.values.reshape(-1, 1))
    
    yDiff = rpcImonData.Imon - yPredict
    
    fig = plt.figure(figsize=(14, 8))
    ax1 = plt.subplot(221)
    ax1.plot(rpcImonData.Imon_change_date, rpcImonData.Imon, '.', label="measured")
    ax1.plot(rpcImonData.Imon_change_date, yPredict, '.', label="predicted")
    ax1.set_xlabel("Predict VS Measured, axis-x: Imon_change_date, axis-y: Imon")
    ax1.legend()
    
    ax2 = plt.subplot(223)
    ax2.plot(rpcImonData.inst_lumi, rpcImonData.Imon, '.', label="measured")
    ax2.plot(rpcImonData.inst_lumi, yPredict, '.', label="predicted")
    ax2.set_xlabel("Predict VS Measured axis-x: inst_lumi, axis-y: Imon")
    ax2.legend()
    
    ax3 = plt.subplot(122)
    ax3.hist(yDiff, bins=100)
    ax3.set_xlabel(f"(Measured - Predict) Histogram(Imon), Bins=100")
    ax3.annotate(f"Mean: {np.mean(yDiff)} \n Mean(abs): {np.mean(np.abs(yDiff))}", xy=(1, 1), xycoords='axes fraction', fontsize=10, \
    horizontalalignment='right', verticalalignment='bottom')

    plt.suptitle(f"Chamber, Year: {dpidName[0:-4]} \nRegression Condition: \n(inst_lumi: All Data, Intercept: True) \n After DBSCAN")
    plt.tight_layout()
    plt.savefig(plotPath + dpidName[0:-4] + ".png")
    plt.close()


if __name__ == "__main__":
    rpcImonPath = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/"
    plotPath = "/Users/mainroot/RPC_graph/SLR/I-L_fitting_AfterDBSCAN/GoldenData/"
    rpcImonSepFolders = os.listdir(rpcImonPath)
    rpcImonSepPaths, plotSepPaths = [], []
    for folder in rpcImonSepFolders:
        rpcImonSepPaths.append(rpcImonPath + folder + "/")
        plotSepPaths.append(plotPath + folder + "/")

    for i in range(len(rpcImonSepPaths)):
        dpidNames = os.listdir(rpcImonSepPaths[i])
        pool = multiprocessing.Pool(6)
        m = multiprocessing.Manager()
        pool.starmap(plotFunction, [(rpcImonSepPaths[i], plotSepPaths[i], dpidName) for dpidName in dpidNames])
        pool.close()
        pool.join()