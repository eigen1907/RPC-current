import matplotlib.pyplot as plt
import pandas as pd
import os


rpcImonPath = "/Users/mainroot/RPC_modified_data/SecondaryArrangement/GoldenRPC/2018/dpid_3010_2018.csv"
rpcImonData = pd.read_csv(rpcImonPath)

rpcImonData.Imon_change_date = pd.to_datetime(rpcImonData.Imon_change_date)

rpcImonData1 = rpcImonData[(rpcImonData.Imon_change_date > pd.to_datetime("2018-07-27")) & (rpcImonData.Imon_change_date < pd.to_datetime("2018-08-19 22:00:00"))]
rpcImonData2 = rpcImonData[(rpcImonData.Imon_change_date < pd.to_datetime("2018-07-27")) | (rpcImonData.Imon_change_date > pd.to_datetime("2018-08-19 22:00:00"))]
#7월 27일 ~ 8월 19일 22시

ax1 = plt.subplot(221)
ax1.plot(rpcImonData1.Imon_change_date, rpcImonData1.Vmon, '.')
ax1.plot(rpcImonData2.Imon_change_date, rpcImonData2.Vmon, '.')
ax1.set_xlabel("axis-y: Vmon, axis-x: date")

ax2 = plt.subplot(223)
ax2.plot(rpcImonData1.Imon_change_date, rpcImonData1.Vmon/rpcImonData1.press, '.')
ax2.plot(rpcImonData2.Imon_change_date, rpcImonData2.Vmon/rpcImonData2.press, '.')
ax2.set_xlabel("axis-y: Vmon/press, axis-x: date")

ax3 = plt.subplot(122)
ax3.plot(rpcImonData1.press, rpcImonData1.Vmon, '.')
ax3.plot(rpcImonData2.press, rpcImonData2.Vmon, '.')
ax3.set_xlabel("axis-y: Vmon, axis-x: press")

plt.tight_layout()
plt.show()