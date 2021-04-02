import pandas as pd
import os
import matplotlib.pyplot as plt

## We are ready to analyze the data
### To list up runs:

path = "/Users/mainroot/RPC-test_data/last/"
year = "2018/"

### 많이 찍힌 놈
#dpid = "dpid_389_2018.csv"

### 개판인 놈
#dpid = "dpid_348_2018.csv"

#### 예쁜 놈
dpid = "dpid_354_2018.csv"


dfAll = pd.read_csv(path + year + dpid)

dfAll["Imon_change_date"] = pd.to_datetime(dfAll["Imon_change_date"]) 


for fillNumber in dfAll.fill_number.unique():
    df = dfAll[dfAll.fill_number == fillNumber]
    runNumbers = df.run_number.unique()
    imonValues = df.Imon
    lumiValues = df.inst_lumi

    print('Fill=%d nRun=%d nIMON=%d' % (fillNumber, len(runNumbers), len(imonValues)))
    print(lumiValues)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(16, 10))

    #plt.plot(df.inst_lumi, df.Imon, '.')
    for runNumber in runNumbers:
        dfRun = df[df.run_number == runNumber]
        ax1.set_xlabel('time')
        ax1.set_ylabel('Inst. lumi (nb^-1)')
        ax1.plot(dfRun.Imon_change_date, dfRun.inst_lumi, '.-')

        ax2.set_xlabel('time')
        ax2.set_ylabel('IMON current (uA)')
        ax2.plot(dfRun.Imon_change_date, dfRun.Imon, '.-')

        ax3.set_xlabel('Inst. lumi (nb^-1)')
        ax3.set_ylabel('IMON current (uA)')
        ax3.plot(dfRun.inst_lumi, dfRun.Imon, '.')

        ax4.set_xlabel('VMON voltage (V)')
        ax4.set_ylabel('IMON current (uA)')
        ax4.plot(dfRun.Vmon, dfRun.Imon, '.')

    plt.suptitle(f"{year[0:4]} - {dpid[0:9]} - Fill: {fillNumber}")
    plt.tight_layout()
    plt.show()



### You can draw values collapsing everything
#runNumbers = dfAll.run_number.unique()
#fillNumbers = dfAll.fill_number.unique()
#df = dfAll
#plt.plot(df.inst_lumi, df.Imon, '.')
#plt.show()
