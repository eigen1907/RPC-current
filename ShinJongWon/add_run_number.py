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



"""
for i in range(len(filelist_2016)):
    dataset = RPC_module1.dataFromPath(path_2016 + filelist_2016[i])
    dataset.to_csv("ShinJongWon/2016/" + filelist_2016[i], index=False)

for i in range(len(filelist_2017)):
    dataset = RPC_module1.dataFromPath(path_2017 + filelist_2017[i])
    dataset.to_csv("ShinJongWon/2017/" + filelist_2017[i], index=False)
"""



for i in range(len(filelist_2018)):
    dataset = RPC_module1.dataFromPath(path_2018 + filelist_2018[i])
    dataset.to_csv("ShinJongWon/2018/" + filelist_2018[i], index=False)


