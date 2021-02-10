from os import listdir
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
data =[]
directory = listdir('./')
directory = sorted(directory, key = lambda x : int(x.split('_')[1]))
for d in directory:
    names = ['Imon_change_date', 'Imon', 'Vmon', 'inst_lumi', 'lumi_start_date','lumi_end_date', 'Imon_change_date2', 'uxc_change_date', 'temp',
       'press', 'relative_humodity', 'dew_point']
    df = pd.read_csv(d, names=names, parse_dates=['Imon_change_date','Imon_change_date2','lumi_start_date','lumi_end_date','uxc_change_date'])
    data.append(df)
    
print(data[1].shape)


'''
print(directory)
'''
'''
Imon2 =[]
Imon3 =[]
for i in range(len(data)):
    median = np.median(data[i]['Imon'])
    Imon2.append(median)
print(len(Imon2))
plt.plot(Imon2,'.')
#Imon median 찍음
'''
'''
count = []
for i in range(len(data)):
    if np.mean(data[i]['Imon']) > 15:
        count.append(directory[i])
print(count)
'''
'''
#temperature확인 슬롭나누기/ 멀티픽 period나눠보기
Imon2 =[]
Imon3 =[]
tans = []
tans2= []
meanvalue = []
meanvalue2 = []
stdvalue=[]
stdvalue2=[]
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i]['Imon_change_date'][j] = time.mktime(data[i]['Imon_change_date'][j].timetuple())
        if data[i]['inst_lumi'][j] == 'None':
            data[i]['inst_lumi'][j] = 0
        if type(data[i]['inst_lumi'][j]) == str:
            data[i]['inst_lumi'][j] = float(data[i]['inst_lumi'][j])
        if data[i]['Imon_change_date'][j] > 1.4735e9:
            if data[i]['inst_lumi'][j] ==0: continue
            tan = (data[i]['Imon'][j])/data[i]['inst_lumi'][j]
            if  -10<= np.log(tan) <0 :
                tans.append(tan)
        if data[i]['Imon_change_date'][j] < 1.4735e9:
            if data[i]['inst_lumi'][j] ==0: continue
            tan2 = (data[i]['Imon'][j])/data[i]['inst_lumi'][j]
            if  -10<= np.log(tan2) <0 :
                tans2.append(tan2)
    std =np.std(tans)
    std2 = np.std(tans2)
    mean = np.mean(tans)
    mean2 = np.mean(tans2)
    stdvalue.append(std)
    stdvalue2.append(std2)
    meanvalue.append(mean)
    meanvalue2.append(mean2)
    del std
    del std2
    del mean
    del mean2
plt.figure()
plt.hist(stdvalue,100)
plt.hist(stdvalue2,100)
plt.show()
plt.figure()
plt.hist(meanvalue,100)
plt.hist(meanvalue2,100)
plt.show()
'''

'''
Imon2 =[]
Imon3 =[]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i]['inst_lumi'][j] == 'None':
            data[i]['inst_lumi'][j] = 0
        if type(data[i]['inst_lumi'][j]) == str:
            data[i]['inst_lumi'][j] = float(data[i]['inst_lumi'][j])
        if data[i]['inst_lumi'][j] != 0 :
            Imon3.append(data[i]['Imon'][j])
    median = np.median(Imon3)
    Imon2.append(median)
    del Imon3[:]

plt.plot(Imon2)
#Imon median 찍음
'''
'''
Imon_lumi=[]
Imon_lumi2=[]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i]['inst_lumi'][j] == 'None':
            data[i]['inst_lumi'][j] = 0
        if type(data[i]['inst_lumi'][j]) == str:
            data[i]['inst_lumi'][j] = float(data[i]['inst_lumi'][j])
        if data[i]['inst_lumi'][j] != 0 :
            Imon_lumi.append(data[i]['Imon'][j]/data[i]['inst_lumi'][j])
    median = np.median(Imon_lumi)
    Imon_lumi2.append(median)
    del Imon_lumi[:]
print(len(Imon_lumi2))
plt.plot(Imon_lumi2)
#Imon/inst

'''
