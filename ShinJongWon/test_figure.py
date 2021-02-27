import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from RPC_package.RPC_module1 import dataFromPath

path = "../RPC-data/2017/dpid_320_2017.csv"
dataset = dataFromPath(path)

#figure from data
fig, axes = plt.subplots(2, 4)
fig.patch.set_facecolor('w')
fig.set_size_inches((25, 10)) 
axes[0, 0].scatter(dataset['Imon_change_date'], dataset['Imon'], alpha=0.7, s=1.5)
axes[0, 0].set_title("Imon - date")

axes[0, 1].scatter(dataset['Imon_change_date'], dataset['Vmon'], alpha=0.7, s=1.5)
axes[0, 1].set_title("Vmon - date")

axes[0, 2].scatter(dataset['Imon_change_date'], dataset['inst_lumi'], alpha=0.7, s=1.5)
axes[0, 2].set_title("inst_lumi - date")

axes[0, 3].scatter(dataset['Imon_change_date'], dataset['temp'], alpha=0.7, s=1.5)
axes[0, 3].set_title("temp - date")

axes[1, 0].scatter(dataset['Imon_change_date'], dataset['press'], alpha=0.7, s=1.5)
axes[1, 0].set_title("press - date")

axes[1, 1].scatter(dataset['Imon_change_date'], dataset['relative_humodity'], alpha=0.7, s=1.5)
axes[1, 1].set_title("relative_humodity - date")

axes[1, 2].scatter(dataset['Imon_change_date'], dataset['dew_point'], alpha=0.7, s=1.5)
axes[1, 2].set_title("dew_point - date")

axes[1, 3].scatter(dataset['inst_lumi'], dataset['Imon'], alpha=0.7, s=1.5)
axes[1, 3].set_title("Imon - inst_lumi")

plt.suptitle(path[5:-4])

plt.show()

