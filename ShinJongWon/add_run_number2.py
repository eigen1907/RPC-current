import os
import numpy as np
import RPC_module1 as RPC_module1
import pandas as pd


path_2016 = "/Users/mainroot/RPC-current/ShinJongWon/2016/"
path_2017 = "/Users/mainroot/RPC-current/ShinJongWon/2017/"
path_2018 = "/Users/mainroot/RPC-current/ShinJongWon/2018/"


filelist_2016 = os.listdir(path_2016)
filelist_2017 = os.listdir(path_2017)
filelist_2018 = os.listdir(path_2018)


run_data_2016 = pd.read_csv("/Users/mainroot/RPC-data/run_number/run_number_2016.csv")
run_data_2017 = pd.read_csv("/Users/mainroot/RPC-data/run_number/run_number_2017.csv")
run_data_2018 = pd.read_csv("/Users/mainroot/RPC-data/run_number/run_number_2018.csv")


for i in range(len(filelist_2016)):
    data_2016 = pd.read_csv(path_2016 + filelist_2016[i])
    break_point = 0
    data_2016["run_number"] = None
    data_2016["fill_number"] = None
    data_2016["delivered_lumi"] = None
    data_2016["recorded_lumi"] = None
    for j in range(len(data_2016)):
        for k in range(break_point, len(run_data_2016)):
            if data_2016["Imon_change_date"][j] >= run_data_2016["start_time"][k] and data_2016["Imon_change_date"][j] <= run_data_2016["end_time"][k]:
                data_2016["run_number"][j] = run_data_2016["run_number"][k]
                data_2016["fill_number"][j] = run_data_2016["fill_number"][k]
                data_2016["delivered_lumi"][j] = run_data_2016["delivered_lumi"][k]
                data_2016["recorded_lumi"][j] = run_data_2016["recorded_lumi"][k]
                break_point = k
                break

    data_2016.to_csv("ShinJongWon/2016_addrun/" + filelist_2016[i], index=False)


for i in range(len(filelist_2017)):
    data_2017 = pd.read_csv(path_2017 + filelist_2017[i])
    break_point = 0
    data_2017["run_number"] = None
    data_2017["fill_number"] = None
    data_2017["delivered_lumi"] = None
    data_2017["recorded_lumi"] = None
    for j in range(len(data_2017)):
        for k in range(break_point, len(run_data_2017)):
            if data_2017["Imon_change_date"][j] >= run_data_2017["start_time"][k] and data_2017["Imon_change_date"][j] <= run_data_2017["end_time"][k]:
                data_2017["run_number"][j] = run_data_2017["run_number"][k]
                data_2017["fill_number"][j] = run_data_2017["fill_number"][k]
                data_2017["delivered_lumi"][j] = run_data_2017["delivered_lumi"][k]
                data_2017["recorded_lumi"][j] = run_data_2017["recorded_lumi"][k]
                break_point = k
                break

    data_2017.to_csv("ShinJongWon/2017_addrun/" + filelist_2017[i], index=False)


for i in range(len(filelist_2018)):
    data_2018 = pd.read_csv(path_2018 + filelist_2018[i])
    break_point = 0
    data_2018["run_number"] = None
    data_2018["fill_number"] = None
    data_2018["delivered_lumi"] = None
    data_2018["recorded_lumi"] = None
    for j in range(len(data_2018)):
        for k in range(break_point, len(run_data_2018)):
            if data_2018["Imon_change_date"][j] >= run_data_2018["start_time"][k] and data_2018["Imon_change_date"][j] <= run_data_2018["end_time"][k]:
                data_2018["run_number"][j] = run_data_2018["run_number"][k]
                data_2018["fill_number"][j] = run_data_2018["fill_number"][k]
                data_2018["delivered_lumi"][j] = run_data_2018["delivered_lumi"][k]
                data_2018["recorded_lumi"][j] = run_data_2018["recorded_lumi"][k]
                break_point = k
                break

    data_2018.to_csv("ShinJongWon/2018_addrun/" + filelist_2018[i], index=False)


