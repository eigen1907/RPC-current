import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import RPCmodule as RPCmodule


dataset = RPCmodule.dataFromPath("2017/dpid_320_2017.csv")

initial_point = 2950
final_point = 3100


x_plot2 = dataset["Imon_change_date"]
y_plot2 = dataset["Vmon"]


plt.scatter(x_plot2, y_plot2, alpha=0.7, s=1.5)
plt.show()


Vmon_testing_index = []

for i in range(initial_point, final_point):
    if dataset["Vmon"][i] > 9450 or dataset["Vmon"][i] < 9450:
        print(i)
        Vmon_testing_index.append(i)


dataset = dataset.drop(Vmon_testing_index)

print(dataset.head())

x_plot2 = dataset["Imon_change_date"]
y_plot2 = dataset["Vmon"]


plt.scatter(x_plot2, y_plot2, alpha=0.7, s=1.5)
plt.show()


