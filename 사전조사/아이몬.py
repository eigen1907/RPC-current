import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import time
import os
names = ['Imon_change_date', 'Imon', 'Vmon', 'inst_lumi', 'lumi_start_date','lumi_end_date', 'Imon_change_date2', 'uxc_change_date', 'temp',
       'press', 'relative_humodity', 'dew_point']
data =pd.read_csv("C:/Users/https/Desktop/기타/랩실/imon_2016/IMON/20200131_1/barrel_data/2016/dpid_2939_2016.csv", names=names, parse_dates=['Imon_change_date','Imon_change_date2','lumi_start_date','lumi_end_date','uxc_change_date'])
data2 =pd.read_csv("C:/Users/https/Desktop/기타/랩실/imon_2016/IMON/20200131_1/barrel_data/2016/dpid_2938_2016.csv", names=names, parse_dates=['Imon_change_date','Imon_change_date2','lumi_start_date','lumi_end_date','uxc_change_date'])
start = time.time()

data.loc[data['inst_lumi']=='None','inst_lumi'] = 0
data = data.astype({'inst_lumi':'float'})
'''
if type(data['inst_lumi']) == str:
    data['inst_lumi'] = float
print(type(data['inst_lumi'][1]))
print('time : ', time.time()-start)
'''
'''

for i in range(len(data)):
    if data['inst_lumi'][i] == 'None':
        data['inst_lumi'][i] = 0
    if type(data['inst_lumi'][i]) == str:
        data['inst_lumi'][i] = float(data['inst_lumi'][i])
    '''
print("time :",time.time() - start)
print(type(data['inst_lumi'][1]))
    
'''
for i in range(len(data)):
    data['Imon_change_date'][i] = time.mktime(data['Imon_change_date'][i].timetuple())
    data['Imon_change_date2'][i] = time.mktime(data['Imon_change_date2'][i].timetuple())
    data['uxc_change_date'][i] =  time.mktime(data['uxc_change_date'][i].timetuple())
    data['lumi_start_date'][i] =  time.mktime(data['lumi_start_date'][i].timetuple())
    data['lumi_end_date'][i] =  time.mktime(data['lumi_end_date'][i].timetuple())


data['inst_lumi'] = data['inst_lumi'].astype(np.float)

for i in range(11):
    data[data.columns[i]] = data[data.columns[i]].astype(float)
    
#print(data['inst_lumi'].dtype)
#plt.plot(data['Imon_change_date'],data['temp'])

pd.plotting.scatter_matrix(data.all(),figsize=(10,10));
'''
#plt.xlim(1.470e18,1.4705e18)
#plt.plot(data['Imon_change_date'].astype(np.int64),data['inst_lumi'],'.')   

'''
print(type(data['inst_lumi'][10]))


tans = []
times = []
for i in range(len(data)):
    if data['inst_lumi'][i] ==0: continue
    tan = (data['Imon'][i])/data['inst_lumi'][i]
    tans.append(tan)
    times.append(data['Imon_change_date'][i])
 #   print(tan)
print(max(tans))
plt.hist2d(times,tans)
#print(tans)
#plt.xlim(0,)
#plt.yscale('log')
#plt.xscale('log')


plt.hist2d(data['inst_lumi'],data['Imon']-1.5,bins = 20)
'''
#plt.hist(np.log(tans), range=(-11,-2), bins = 500)
#plt.show()
#overflowbin
#cms tdr, rpc검출기 책 도서관\\\\
#inst_lumi에 대한 분포를 그려본다. 그 값이 0인거를 찾아서 그때의 Imon을 그리면 백그라운드가 나오겠지?
#그걸 Imon에서 빼주고 다시 그리면 더 정확한 그림이 나올것이다.
'''
'''
'''
zero = []
for i in range(len(data)):
    if data['inst_lumi'][i] == 0:
        ze = data['Imon'][i]
        zero.append(ze)
#print(zero)
plt.hist(zero,bins=50)
print(np.median(zero))
'''

'''
'''
'''

D = []
for i in range(len(data)):
    if type(data['uxc_change_date'][i]) == float:
        D.append(i)

print(len(D))
'''        
'''
for i in range(11):
    for j in range(len(data)):
        if type(data[data.columns[i]][j]) == str:
            data[data.columns[i]][j] = float(data[data.columns[i]][j])
        if type(data[data.columns[i]][j]) == 'None':
            data[data.columns[i]][j] = 0 


scm = pd.plotting.scatter_matrix(data, figsize=(15,15));
#plt.plot(np.log(data['uxc_change_date']),data['Imon'])       
for ax in scm.ravel():
    ax.set_xlabel(ax.get_xlabel(), fontsize = 9, rotation = 0)
    ax.set_ylabel(ax.get_ylabel(), fontsize = 9, rotation = 0)
'''

