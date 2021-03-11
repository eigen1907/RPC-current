import os
import pandas as pd
import json
import csv
import multiprocessing


PATH2016 = "/Users/mainroot/RPC-test_data/runCertification/2016_271036-284044.json"
PATH2017 = "/Users/mainroot/RPC-test_data/runCertification/2017_294927-306462.json"
PATH2018 = "/Users/mainroot/RPC-test_data/runCertification/2018_314472-325175.json"


with open(PATH2016) as json_data:
    data2016 = json.load(json_data)

with open(PATH2017) as json_data:
    data2017 = json.load(json_data)

with open(PATH2018) as json_data:
    data2018 = json.load(json_data)

new_data2016 = []
new_data2017 = []
new_data2018 = []

for key, value in data2016.items():
    total_list = []
    total_list.append(key)
    total_list.append(value)
    new_data2016.append(total_list)

for key, value in data2017.items():
    total_list = []
    total_list.append(key)
    total_list.append(value)
    new_data2017.append(total_list)


for key, value in data2018.items():
    total_list = []
    total_list.append(key)
    total_list.append(value)
    new_data2018.append(total_list)



df2016 = pd.DataFrame(new_data2016)
df2017 = pd.DataFrame(new_data2017)
df2018 = pd.DataFrame(new_data2018)

set_column = ["run_number", "cert_lumi_section"]

df2016.columns = set_column
df2017.columns = set_column
df2018.columns = set_column


for i in range(len(df2016)):
    for j in range(len(df2016["cert_lumi_section"][i])):
        df2016["cert_lumi_section"][i][j][0] -= 1
        df2016["cert_lumi_section"][i][j][0] *= 23.3108931
        df2016["cert_lumi_section"][i][j][1] *= 23.3108931
        df2016["cert_lumi_section"][i][j][0] = round(df2016["cert_lumi_section"][i][j][0])
        df2016["cert_lumi_section"][i][j][1] = round(df2016["cert_lumi_section"][i][j][1])

for i in range(len(df2017)):
    for j in range(len(df2017["cert_lumi_section"][i])):
        df2017["cert_lumi_section"][i][j][0] -= 1
        df2017["cert_lumi_section"][i][j][0] *= 23.3108931
        df2017["cert_lumi_section"][i][j][1] *= 23.3108931
        df2017["cert_lumi_section"][i][j][0] = round(df2017["cert_lumi_section"][i][j][0])
        df2017["cert_lumi_section"][i][j][1] = round(df2017["cert_lumi_section"][i][j][1])

for i in range(len(df2018)):
    for j in range(len(df2018["cert_lumi_section"][i])):
        df2018["cert_lumi_section"][i][j][0] -= 1
        df2018["cert_lumi_section"][i][j][0] *= 23.3108931
        df2018["cert_lumi_section"][i][j][1] *= 23.3108931
        df2018["cert_lumi_section"][i][j][0] = round(df2018["cert_lumi_section"][i][j][0])
        df2018["cert_lumi_section"][i][j][1] = round(df2018["cert_lumi_section"][i][j][1])


run_df2016 = pd.read_csv("/Users/mainroot/RPC-test_data/run_data/2016.csv")
run_df2017 = pd.read_csv("/Users/mainroot/RPC-test_data/run_data/2017.csv")
run_df2018 = pd.read_csv("/Users/mainroot/RPC-test_data/run_data/2018.csv")


run_df2016 = run_df2016.drop(columns=["Unnamed: 0", "fill_number", "duration", "end_time", "delivered_lumi", "recorded_lumi", "l1_triggers_counter"
, "l1_hlt_mode_stripped", "hlt_key", "initial_prescale_index"])
run_df2017 = run_df2017.drop(columns=["Unnamed: 0", "fill_number", "duration", "end_time", "delivered_lumi", "recorded_lumi", "l1_triggers_counter"
, "l1_hlt_mode_stripped", "hlt_key", "initial_prescale_index"])
run_df2018 = run_df2018.drop(columns=["Unnamed: 0", "fill_number", "duration", "end_time", "delivered_lumi", "recorded_lumi", "l1_triggers_counter"
, "l1_hlt_mode_stripped", "hlt_key", "initial_prescale_index"])


new_df2016 = pd.DataFrame(index=range(0, 631), columns=["run_number", "cert_start_time", "cert_end_time"])
new_df2017 = pd.DataFrame(index=range(0, 828), columns=["run_number", "cert_start_time", "cert_end_time"])
new_df2018 = pd.DataFrame(index=range(0, 760), columns=["run_number", "cert_start_time", "cert_end_time"])

count = 0
j = 0   
for i in range(len(new_df2016)):
    if j > 393:
        break
    new_df2016["run_number"][i] = int(df2016["run_number"][j])
    new_df2016["cert_start_time"][i] = df2016["cert_lumi_section"][j][0][0]
    new_df2016["cert_end_time"][i] = df2016["cert_lumi_section"][j][0][1]
    count += 1
    if count == len(df2016["cert_lumi_section"][j]):
        count = 0
        j += 1

count = 0
j = 0   
for i in range(len(new_df2017)):
    if j > 474:
        break
    new_df2017["run_number"][i] = int(df2017["run_number"][j])
    new_df2017["cert_start_time"][i] = df2017["cert_lumi_section"][j][0][0]
    new_df2017["cert_end_time"][i] = df2017["cert_lumi_section"][j][0][1]
    count += 1
    if count == len(df2017["cert_lumi_section"][j]):
        count = 0
        j += 1

count = 0
j = 0   
for i in range(len(new_df2018)):
    if j > 478:
        break
    new_df2018["run_number"][i] = int(df2018["run_number"][j])
    new_df2018["cert_start_time"][i] = df2018["cert_lumi_section"][j][0][0]
    new_df2018["cert_end_time"][i] = df2018["cert_lumi_section"][j][0][1]
    count += 1
    if count == len(df2018["cert_lumi_section"][j]):
        count = 0
        j += 1



run_df2016 = run_df2016.astype({"run_number": "int"})
run_df2017 = run_df2017.astype({"run_number": "int"})
run_df2018 = run_df2018.astype({"run_number": "int"})



new_df2016 = pd.merge(new_df2016, run_df2016, on="run_number")
new_df2017 = pd.merge(new_df2017, run_df2017, on="run_number")
new_df2018 = pd.merge(new_df2018, run_df2018, on="run_number")


print(run_df2016.info())
print()
print()
print(new_df2016.info())


new_df2016.to_csv("cert_run2016.csv", index=False)
new_df2017.to_csv("cert_run2017.csv", index=False)
new_df2018.to_csv("cert_run2018.csv", index=False)




