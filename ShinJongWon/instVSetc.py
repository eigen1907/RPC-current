import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "/Users/mainroot/RPC-test_data/2016_addrun/dpid_319_2016.csv"
dataset = pd.read_csv(path)

print(dataset.head())
"""
plt.scatter(dataset["Imon_change_date"], dataset["inst_lumi"], s=2.0)
plt.show()
"""
