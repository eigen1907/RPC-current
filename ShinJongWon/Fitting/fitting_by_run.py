import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os



path = "/Users/mainroot/RPC-test_data/cert_data/2018_final/dpid_322_2018.csv"
path2 = "/Users/mainroot/RPC-test_data/addrun2/2018_addrun2/dpid_322_2018.csv"


data = pd.read_csv(path)
data2 = pd.read_csv(path)

fill_groups = data.groupby("fill_number")
fill_groups2 = data2.groupby("fill_number")

"""
is_fill = data["fill_number"] == wanted_number

fill_data = data[is_fill]

plt.scatter(fill_data["Imon_change_date"], fill_data["Imon"], s=1.5)
plt.show()
"""


for fill_name, fill_group in fill_groups:
    run_groups = fill_group.groupby("run_number")
    fig, ax = plt.subplots(figsize=[16, 10])
    for run_name, run_group in run_groups:
        ax.plot(
            run_group.Imon_change_date,
            run_group.Imon,
            marker = "o",
            linestyle = "",
            label = "run_number: " + str(run_name)
        )
    ax.legend(fontsize=12, loc="upper left")
    plt.title(f"Fill number: {fill_name}", fontsize=20)
    plt.xlabel("Imon_change_date", fontsize=12)
    plt.ylabel("inst_lumi", fontsize=12)
    plt.show()



