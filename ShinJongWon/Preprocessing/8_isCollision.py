import os
import pandas as pd
import csv

run_data2016 = pd.read_csv("/Users/mainroot/RPC-test_data/run_data/2016.csv")
run_data2017 = pd.read_csv("/Users/mainroot/RPC-test_data/run_data/2017.csv")
run_data2018 = pd.read_csv("/Users/mainroot/RPC-test_data/run_data/2018.csv")




run_data2016 = run_data2016.drop(columns="Unnamed: 0")
run_data2017 = run_data2017.drop(columns="Unnamed: 0")
run_data2018 = run_data2018.drop(columns="Unnamed: 0")

is_collision2016 = []
is_collision2017 = []
is_collision2018 = []

for i in range(len(run_data2016)):
    hlt_key = str(run_data2016["l1_hlt_mode_stripped"][i])
    if hlt_key[0:9] == "collision":
        is_collision2016.append(True)
    else:
        is_collision2016.append(False)

for i in range(len(run_data2017)):
    hlt_key = str(run_data2017["l1_hlt_mode_stripped"][i])
    if hlt_key[0:9] == "collision":
        is_collision2017.append(True)
    else:
        is_collision2017.append(False)

for i in range(len(run_data2018)):
    hlt_key = str(run_data2018["l1_hlt_mode_stripped"][i])
    if hlt_key[0:9] == "collision":
        is_collision2018.append(True)
    else:
        is_collision2018.append(False)


collision2016 = run_data2016[is_collision2016]
collision2017 = run_data2017[is_collision2017]
collision2018 = run_data2018[is_collision2018]

print(len(collision2016))
print(len(collision2017))
print(len(collision2018))

collision2016 = collision2016.astype({"run_number": "int", "fill_number": "int"})
collision2017 = collision2017.astype({"run_number": "int", "fill_number": "int"})
collision2018 = collision2018.astype({"run_number": "int", "fill_number": "int"})


collision2016.to_csv("/Users/mainroot/RPC-test_data/run_data/collisions2016.csv", index=False)
collision2017.to_csv("/Users/mainroot/RPC-test_data/run_data/collisions2017.csv", index=False)
collision2018.to_csv("/Users/mainroot/RPC-test_data/run_data/collisions2018.csv", index=False)



