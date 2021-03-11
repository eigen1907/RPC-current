import os
import numpy as np
import matplotlib.pyplot as plt
import RPC_module1 as RPC_module1
import pandas as pd


path_2016 = "/Users/mainroot/RPC-data/2016/"
path_2017 = "/Users/mainroot/RPC-data/2017/"
path_2018 = "/Users/mainroot/RPC-data/2018/"


filelist_2016 = os.listdir(path_2016)
filelist_2017 = os.listdir(path_2017)
filelist_2018 = os.listdir(path_2018)


for i in range(len(filelist_2016)):
    dataset = RPC_module1.dataFromPath(path_2016 + filelist_2016[i])
    dataset.to_csv("/Users/mainroot/RPC-test_data/2016/" + filelist_2016[i], index=False)

for i in range(len(filelist_2017)):
    dataset = RPC_module1.dataFromPath(path_2017 + filelist_2017[i])
    dataset.to_csv("/Users/mainroot/RPC-test_data/2017/" + filelist_2017[i], index=False)

for i in range(len(filelist_2018)):
    dataset = RPC_module1.dataFromPath(path_2018 + filelist_2018[i])
    dataset.to_csv("/Users/mainroot/RPC-test_data/2018/" + filelist_2018[i], index=False)


run_path_2016 = "/Users/mainroot/RPC-data/run_number/run_number_2016.csv"
run_path_2017 = "/Users/mainroot/RPC-data/run_number/run_number_2017.csv"
run_path_2018 = "/Users/mainroot/RPC-data/run_number/run_number_2018.csv"


runData2016 = RPC_module1.dataFromPath2(run_path_2016)
runData2017 = RPC_module1.dataFromPath2(run_path_2017)
runData2018 = RPC_module1.dataFromPath2(run_path_2018)


runData2016.to_csv("/Users/mainroot/RPC-test_data/run_data/2016")
runData2017.to_csv("/Users/mainroot/RPC-test_data/run_data/2017")
runData2018.to_csv("/Users/mainroot/RPC-test_data/run_data/2018")

