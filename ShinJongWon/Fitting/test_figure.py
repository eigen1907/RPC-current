import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def figure(dataset):
    dataset['Imon_change_date'] = pd.to_datetime(dataset['Imon_change_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    dataset['lumi_start_date'] = pd.to_datetime(dataset['lumi_start_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    dataset['lumi_end_date'] = pd.to_datetime(dataset['lumi_end_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    dataset['Imon_change_date2'] = pd.to_datetime(dataset['Imon_change_date2'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    dataset['uxc_change_date'] = pd.to_datetime(dataset['uxc_change_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
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

    plt.show()


origin_data = pd.read_csv("/Users/mainroot/RPC-test_data/original/2016/dpid_315_2016.csv")
cert_data = pd.read_csv("/Users/mainroot/RPC-test_data/cert_data/2016test/dpid_315_2016.csv")

figure(origin_data)
figure(cert_data)

