import pandas as pd
import numpy as np



rpcImonFile = "/Users/mainroot/RPC_origin_data/2016/dpid_315_2016.csv"



columnList = ['Imon_change_date', 'Imon', 'Vmon', 'inst_lumi', 'lumi_start_date', 'lumi_end_date', 
'Imon_change_date2', 'uxc_change_date', 'temp', 'press', 'relative_humodity', 'dew_point']
dateDtypeList = ['Imon_change_date', 'lumi_start_date', 'lumi_end_date', 'Imon_change_date2', 'uxc_change_date']
floatDtypeList = ['Imon', 'Vmon', 'inst_lumi', 'temp', 'press', 'relative_humodity', 'dew_point']
dateDtypeDict = {dateDtype: pd.Timestamp for dateDtype in dateDtypeList}
floatDtypeDict = {floatDtype: np.float for floatDtype in floatDtypeList}
dtypeDict = dict(dateDtypeDict, **floatDtypeDict)

print(dtypeDict)
print("="*80)

rpcImonData = pd.read_csv(
    rpcImonFile,
    sep = ',',
    names=columnList,
    parse_dates=dateDtypeList,
    infer_datetime_format=True
)

rpcImonData = rpcImonData.drop(columns=['Imon_change_date2'])
rpcImonData = rpcImonData.dropna()

print(rpcImonData.head())
print(rpcImonData.info())


