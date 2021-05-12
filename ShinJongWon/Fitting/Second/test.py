import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

rpcImonData = pd.read_csv("/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPCSeparate/2016_former/dpid_327_2016.csv")
rpcImonData["Imon_change_date"] = pd.to_datetime(rpcImonData["Imon_change_date"])

#plt.plot(rpcImonData.inst_lumi, rpcImonData.Imon, ".")
#plt.show()

"""
from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=2, random_state=42, verbose=1, tol=1e-6)

x1 = rpcImonData["Imon"]
x2 = rpcImonData["inst_lumi"]
X = pd.concat([x1, x2], ignore_index=True, axis=1)


gmm_labels = gmm.fit_predict(X)

rpcImonData["gmm_cluster"] = gmm_labels

plt.plot(rpcImonData[rpcImonData["gmm_cluster"] == 0].inst_lumi, rpcImonData[rpcImonData["gmm_cluster"] == 0].Imon, ".")
plt.plot(rpcImonData[rpcImonData["gmm_cluster"] == 1].inst_lumi, rpcImonData[rpcImonData["gmm_cluster"] == 1].Imon, ".")
plt.plot(rpcImonData[rpcImonData["gmm_cluster"] == 2].inst_lumi, rpcImonData[rpcImonData["gmm_cluster"] == 2].Imon, ".")
plt.show()


"""
from sklearn.cluster import DBSCAN


x1 = rpcImonData["Imon"]
x1Max = max(x1)

x2 = rpcImonData["inst_lumi"]
x2Max = max(x2)

x1Norm = x1 / x1Max
x2Norm = x2 / x2Max

X = pd.concat([x1Norm, x2Norm], ignore_index=True, axis=1)
model = DBSCAN(eps=0.08, min_samples=50)
model_labels = model.fit_predict(X)

print(np.unique(model_labels))

rpcImonData["label"] = model_labels



plt.plot(rpcImonData[rpcImonData["label"] == 0].inst_lumi, rpcImonData[rpcImonData["label"] == 0].Imon, ".", label="i = 0")
plt.plot(rpcImonData[rpcImonData["label"] != 0].inst_lumi, rpcImonData[rpcImonData["label"] != 0].Imon, ".", label="i != 0")
plt.legend()
plt.show()



