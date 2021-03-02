import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


path = "/Users/mainroot/RPC-test_data/2016_sep"
dpidList = os.listdir(path)

print(len(dpidList))

for dpid in dpidList:
    fillList = os.listdir(f"{path}/{dpid}")
    for fill in fillList:
        dataset = pd.read_csv(f"{path}/{dpid}/{fill}")
        if len(dataset) > 50:
            groups = dataset.groupby("run_number")
            
            fig, ax = plt.subplots(figsize=[16, 10])
            for name, group in groups:
                ax.plot(
                    group.Imon_change_date,
                    group.Imon,
                    marker = "o",
                    linestyle = "",
                    label = str(name)[0:-2]
                )
            ax.legend(fontsize=12, loc="upper left")
            plt.title("Scatter by Fill, Colered by Run", fontsize=20)
            plt.xticks(np.arange(dataset.iloc[0][0], dataset.iloc[-1][0], step=(dataset.iloc[0][0]-dataset.iloc[-1][0])/5))
            plt.yticks()
            plt.xlabel("Imon_change_date", fontsize=12)
            plt.ylabel("Imon", fontsize=12)
            plt.show()


