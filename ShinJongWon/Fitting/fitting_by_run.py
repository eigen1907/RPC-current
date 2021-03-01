import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("/Users/mainroot/RPC-test_data/2017_addrun/dpid_323_2017.csv")



is_5950 = dataset["fill_number"] == 5950

fill_5950 = dataset[is_5950]

fill_5950.plot(
    kind = "scatter",
    x = "Imon_change_date",
    y = "Imon",
    s = 10.0,
    c = fill_5950["run_number"],
    colormap = "rainbow"
)


plt.show()

