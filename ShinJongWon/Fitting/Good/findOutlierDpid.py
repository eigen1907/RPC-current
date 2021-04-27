import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import multiprocessing



def figure(rpcImonPath, rpcImonFile, figurePath):
    rpcImonData = pd.read_csv(rpcImonPath + rpcImonFile, low_memory=False)

    rpcImonData["Imon_change_date"] = pd.to_datetime(rpcImonData["Imon_change_date"])
    
    rpcImonData = rpcImonData.drop(columns=['lumi_start_date', 'lumi_end_date', 'uxc_change_date', 'dew_point', 'relative_humodity'])

    fig = plt.figure(figsize=(14, 8))
    ax1 = plt.subplot(221)
    ax1.plot(rpcImonData.Imon_change_date, rpcImonData.Imon, '.')
    ax1.set_xlabel("axis-x: Imon_change_date, axis-y: Imon")

    ax2 = plt.subplot(222)
    ax2.plot(rpcImonData.Imon_change_date, rpcImonData.inst_lumi, '.')
    ax2.set_xlabel("axis-x: Imon_change_date, axis-y: inst_lumi")

    ax3 = plt.subplot(223)
    ax3.plot(rpcImonData.Imon_change_date, rpcImonData.Vmon/rpcImonData.press, '.')
    ax3.set_xlabel("axis-x: Imon_change_date, axis-y: Vmon/press")

    ax4 = plt.subplot(224)
    ax4.plot(rpcImonData.inst_lumi, rpcImonData.Imon, '.')
    ax4.set_xlabel("axis-x: inst_lumi, axis-y: Imon")

    plt.suptitle(f"{rpcImonFile[0:-4]}")
    plt.tight_layout()
    plt.savefig(figurePath + rpcImonFile[0:-4] + ".png")
    plt.close()


if __name__ == "__main__":
    rpcImonPath = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/Original/2017/"
    figurePath = "/Users/mainroot/RPC_graph/FindOutlierDpid/2017/"
    rpcImonFiles = os.listdir(rpcImonPath)

    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    pool.starmap(figure, [(rpcImonPath, rpcImonFile, figurePath) for rpcImonFile in rpcImonFiles])
    pool.close()
    pool.join()