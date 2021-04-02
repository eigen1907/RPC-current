import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib as mpl


path2017 = "/Users/mainroot/RPC-test_data/last/2017/"
fileList = os.listdir(path2017)


IOverLMedianList = []
IOverLExpMedianList = []
expVOverPMedianList = []
LexpVOverPMedianList = []
fillNumList = []

for fileName in fileList:
    dfAll = pd.read_csv(path2017 + fileName)
    for colName in ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']:
        dfAll[colName] = pd.to_datetime(dfAll[colName])
    for fillNumber in dfAll.fill_number.unique():
        df = dfAll[dfAll.fill_number == fillNumber]
        IOverLMedianList.append(np.nanmedian(df.Imon / df.inst_lumi))
        IOverLExpMedianList.append(np.nanmedian(df.Imon / (np.exp(df.Vmon / df.press) * df.inst_lumi)))
        expVOverPMedianList.append(np.nanmedian(np.exp(df.Vmon / df.press)))
        LexpVOverPMedianList.append(np.nanmedian(np.exp(df.Vmon / df.press) * df.inst_lumi))
        fillNumList.append(fillNumber)





fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(16, 10))
ax1.hist2d(fillNumList, IOverLMedianList, norm=mpl.colors.LogNorm(), bins=50)
ax1.set_xlabel("Fill Number")
ax1.set_ylabel("I / L")

ax2.hist2d(fillNumList, IOverLExpMedianList, norm=mpl.colors.LogNorm(), bins=50)
ax2.set_xlabel("Fill Number")
ax2.set_ylabel("I / L * exp(Vmon/P)")

ax3.hist2d(fillNumList, expVOverPMedianList, norm=mpl.colors.LogNorm(), bins=50)
ax3.set_xlabel("Fill Number")
ax3.set_ylabel("exp(V/P)")

ax4.hist2d(fillNumList, LexpVOverPMedianList, norm=mpl.colors.LogNorm(), bins=50)
ax4.set_xlabel("Fill Number")
ax4.set_ylabel("L * exp(V/P)")


plt.suptitle("Histogram of median value by each fill (All dpid)(2017)")
plt.tight_layout()
plt.show()


print("="*80)
print(np.nanmean(IOverLMedianList))
print(np.nanmax(IOverLMedianList))
print(np.nanmin(IOverLMedianList))
print("="*80)
print(np.nanmean(IOverLExpMedianList))
print(np.nanmax(IOverLExpMedianList))
print(np.nanmin(IOverLExpMedianList))
print("="*80)
print(np.nanmean(expVOverPMedianList))
print(np.nanmax(expVOverPMedianList))
print(np.nanmin(expVOverPMedianList))
print("="*80)
print(np.nanmean(LexpVOverPMedianList))
print(np.nanmax(LexpVOverPMedianList))
print(np.nanmin(LexpVOverPMedianList))
print("="*80)
        