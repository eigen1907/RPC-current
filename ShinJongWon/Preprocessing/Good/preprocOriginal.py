import json
import pandas as pd
import numpy as np
import os
import multiprocessing


def preprocOriginal(rpcImonFile, outputFile):
    columnList = ['Imon_change_date', 'Imon', 'Vmon', 'inst_lumi', 'lumi_start_date', 'lumi_end_date', 
    'Imon_change_date2', 'uxc_change_date', 'temp', 'press', 'relative_humodity', 'dew_point']
    dateDtypeList = ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'uxc_change_date']
    floatDtypeList = ['Imon', 'Vmon', 'inst_lumi', 'temp', 'press', 'relative_humodity', 'dew_point']
    try:
        rpcImonData = pd.read_csv(
            rpcImonFile,
            names=columnList,
            low_memory=False
        )
    except:
        print("="*100)
        print("read_csv error")
        print(rpcImonFile)
    
    rpcImonData = rpcImonData.drop(columns=['Imon_change_date2'])
    rpcImonData = rpcImonData.dropna()

    for colName in dateDtypeList:
        rpcImonData[colName] = pd.to_datetime(rpcImonData[colName])

    for colName in floatDtypeList:
        rpcImonData[colName] = pd.to_numeric(rpcImonData[colName], errors='coerce', downcast='float')
    
    rpcImonData = rpcImonData.dropna()


if __name__ == "__main__":
    IN_PATH_2016 = "/Users/mainroot/RPC_origin_data/2016/"
    IN_PATH_2017 = "/Users/mainroot/RPC_origin_data/2017/"
    IN_PATH_2018 = "/Users/mainroot/RPC_origin_data/2018/"

    OUT_PATH_2016 = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/Original/2016/"
    OUT_PATH_2017 = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/Original/2017/"
    OUT_PATH_2018 = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/Original/2018/"

    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    fileList = os.listdir(IN_PATH_2016)
    pool.starmap(preprocOriginal, [(IN_PATH_2016 + fileName, OUT_PATH_2016 + fileName) for fileName in fileList])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    fileList= os.listdir(IN_PATH_2017)
    pool.starmap(preprocOriginal, [(IN_PATH_2017 + fileName, OUT_PATH_2017 + fileName) for fileName in fileList])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    fileList= os.listdir(IN_PATH_2018)
    pool.starmap(preprocOriginal, [(IN_PATH_2018 + fileName, OUT_PATH_2018 + fileName) for fileName in fileList])
    pool.close()
    pool.join()
