import os
import numpy as np
import pandas as pd
from numba import jit


path_2016 = "/Users/mainroot/RPC-test_data/2016_addrun/"
path_2017 = "/Users/mainroot/RPC-test_data/2017_addrun/"
path_2018 = "/Users/mainroot/RPC-test_data/2018_addrun/"


filelist_2016 = os.listdir(path_2016)
filelist_2017 = os.listdir(path_2017)
filelist_2018 = os.listdir(path_2018)




for i in range(len(filelist_2016)):
    os.makedirs("ShinJongWon/2016/" + filelist_2016[i][0:-4])
    dataset = pd.read_csv(path_2016 + filelist_2016[i])
    groups = dataset.groupby(dataset.fill_number)
    for name, group in groups:
        group.to_csv(f"ShinJongWon/2016/{filelist_2016[i][0:-4]}/fill{int(name)}.csv")



for i in range(len(filelist_2017)):
    os.makedirs("ShinJongWon/2017/" + filelist_2017[i][0:-4])
    dataset = pd.read_csv(path_2017 + filelist_2017[i])
    groups = dataset.groupby(dataset.fill_number)
    for name, group in groups:
        group.to_csv(f"ShinJongWon/2017/{filelist_2017[i][0:-4]}/fill{int(name)}.csv")


for i in range(len(filelist_2018)):
    os.makedirs("ShinJongWon/2018/" + filelist_2018[i][0:-4])
    dataset = pd.read_csv(path_2018 + filelist_2018[i])
    groups = dataset.groupby(dataset.fill_number)
    for name, group in groups:
        group.to_csv(f"ShinJongWon/2018/{filelist_2018[i][0:-4]}/fill{int(name)}.csv")

        

        
