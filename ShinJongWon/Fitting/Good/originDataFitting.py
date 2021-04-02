import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


rpcImonPath = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/Original/2017/"

dpidName = "dpid_324_2017.csv"

rpcImonData = pd.read_csv(rpcImonPath + dpidName, low_memory=False)

for colName in ['Imon_change_date','lumi_start_date','lumi_end_date','uxc_change_date']:
    rpcImonData[colName] = pd.to_datetime(rpcImonData[colName])

plotX = rpcImonData.Imon_change_date
plotY = rpcImonData.Vmon / rpcImonData.press


plt.figure(figsize=(16,8))
plt.plot(plotX, plotY, ".")
plt.xlabel(plotX.name)
plt.ylabel(plotY.name)
plt.title(dpidName[0:-4])
plt.show()


