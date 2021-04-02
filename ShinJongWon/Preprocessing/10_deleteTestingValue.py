import json
import pandas as pd
import multiprocessing
import os


# for 2017

def deleteTestingValue(rpcIMONFileName, outFileName):
    rpcIMONs = pd.read_csv(rpcIMONFileName)

    for colName in ['Imon_change_date','lumi_start_date','lumi_end_date','uxc_change_date']:
        rpcIMONs[colName] = pd.to_datetime(rpcIMONs[colName])

    rpcIMONs = rpcIMONs[(rpcIMONs.Imon_change_date < pd.to_datetime("2017-09-26 11:00:00")) | (rpcIMONs.Imon_change_date > pd.to_datetime("2017-09-26 16:00:00"))]
    rpcIMONs.to_csv(outFileName, index=False)
    

if __name__ == "__main__":
    IN_PATH_2017 = "/Users/mainroot/RPC_modified_data/golden/2017/"

    OUT_PATH_2017 = "/Users/mainroot/RPC_modified_data/goldenNoTesting/2017/"

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2017)
    pool.starmap(deleteTestingValue, [(IN_PATH_2017 + filename, OUT_PATH_2017 + filename) for filename in filelist])
    pool.close()
    pool.join()


#for 2018
"""
def deleteTestingValue(rpcIMONFileName, outFileName):
    rpcIMONs = pd.read_csv(rpcIMONFileName)

    for colName in ['Imon_change_date','lumi_start_date','lumi_end_date','uxc_change_date']:
        rpcIMONs[colName] = pd.to_datetime(rpcIMONs[colName])

    rpcIMONs = rpcIMONs[(rpcIMONs.Imon_change_date < pd.to_datetime("2018-06-07 06:00:00")) | (rpcIMONs.Imon_change_date > pd.to_datetime("2018-06-09 06:00:00"))]
    rpcIMONs.to_csv(outFileName, index=False)
    

if __name__ == "__main__":
    IN_PATH_2018 = "/Users/mainroot/RPC_modified_data/golden/2018/"

    OUT_PATH_2018 = "/Users/mainroot/RPC_modified_data/goldenNoTesting/2018/"

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2018)
    pool.starmap(deleteTestingValue, [(IN_PATH_2018 + filename, OUT_PATH_2018 + filename) for filename in filelist])
    pool.close()
    pool.join()
"""