import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import time

names = ['Imon_change_date', 'Imon', 'Vmon', 'inst_lumi', 'lumi_start_date','lumi_end_date', 'Imon_change_date2', 'uxc_change_date', 'temp',
       'press', 'relative_humodity', 'dew_point']
data =pd.read_csv("C:/Users/https/Desktop/기타/랩실/imon_2016/IMON/20200131_1/barrel_data/2016/dpid_2944_2016.csv", names=names, parse_dates=['Imon_change_date','Imon_change_date2','lumi_start_date','lumi_end_date','uxc_change_date'])
#


for i in range(len(data)):
    if data['inst_lumi'][i] == 'None':
        data['inst_lumi'][i] = 0
    if type(data['inst_lumi'][i]) == str:
        data['inst_lumi'][i] = float(data['inst_lumi'][i])

for i in range(len(data)):
    data['Imon_change_date'][i] = time.mktime(data['Imon_change_date'][i].timetuple())
  #  data['Imon_change_date2'][i] = time.mktime(data['Imon_change_date2'][i].timetuple())
   # data['uxc_change_date'][i] =  time.mktime(data['uxc_change_date'][i].timetuple())
   # data['lumi_start_date'][i] =  time.mktime(data['lumi_start_date'][i].timetuple())
   # data['lumi_end_date'][i] =  time.mktime(data['lumi_end_date'][i].timetuple())


data['inst_lumi'] = data['inst_lumi'].astype(np.float)
#plt.plot(data['inst_lumi'],'.')
'''
for i in range(11):
    data[data.columns[i]] = data[data.columns[i]].astype(float)
  '''
#under over flow
  
'''
gf = []
gf2=[]
for i in range(len(data)):
    if data['Imon_change_date'][i]>1.535e9:
        gf.append(data['Vmon'][i])
        gf2.append(data['press'][i])
plt.plot(gf2,gf,'.')
'''      
    
tans = []
tans2=[]
overtan = []
undertan=[]
for i in range(len(data)):
    if data['inst_lumi'][i] ==0: continue
    if data['Imon_change_date'][i] > 1.4735e9:
        tan = (data['Imon'][i])/data['inst_lumi'][i]
        if np.log(tan) > 0:
            tan = 1
            overtan.append(i)
        if np.log(tan) <= -10:
            tan = np.exp(-10)
            undertan.append(i)  
        if -10<np.log(tan) <0:
            tans.append(tan)
    if data['Imon_change_date'][i] < 1.4735e9:
        tan = (data['Imon'][i])/data['inst_lumi'][i]
        if np.log(tan) > 0:
            tan = 1
            overtan.append(i)
        if np.log(tan) <= -10:
            tan = np.exp(-10)
            undertan.append(i)   
        if -10<np.log(tan) <0:
            tans2.append(tan)
   # if -10<=np.log(tan) <0:
print(len(overtan),len(undertan))
mean = np.mean(tans)
mean2 = np.mean(tans2)
tans = tans
tans2 = tans2
print(len(tans),len(tans2))

plt.figure()
plt.hist(tans,range=(0,0.02), bins= 100)
plt.figure()
plt.hist(tans2,range=(0,0.02), bins= 100)
plt.figure()
plt.hist(tans-mean,range = (-0.02,0), bins= 100)
plt.figure()
plt.hist(tans2-mean2,range = (-0.02,0), bins= 100)
print(len(tans-mean2))



'''
for i in range (len(tans)):
    if tans2[i] == 0.9800649135079617:
        #ln.append(tans2[i])
        print(i)
'''
  #  times.append(data['Imon_change_date'][i])
  #  mean =np.mean(tans)
        #print(i)
'''    
    if data['Imon_change_date'][i] < 1.467e9:
        if data['inst_lumi'][i] ==0: continue
        tan2 = (data['Imon'][i])/data['inst_lumi'][i]
        tans2.append(tan2)
        times2.append(data['Imon_change_date'][i])
        mean2 = np.mean(tans2)
'''
'''
#plt.xlim(1.4e9,1.5e9)
#plt.hist(times2,np.log(tans2))


'''
'''
dot=[]
#plt.plot(press,Vmon,'.')
for i in range(len(data)):
    if data['Imon_change_date'][i] > 1.4626e9 and data['Imon_change_date'][i] < 1.4627e9 :
        dot.append(i)
'''
'''



plt.plot(data['press'],data['Vmon'],'.')
'''
'''
#plt.hist(data['Imon'],bins=100)
#plt.hist2d(data['inst_lumi'],data['Imon'],bins = 20)
#print(data['inst_lumi'])
#plt.plot(data['Imon_change_date'],data['temp'])
#plt.hist(data['inst_lumi'],bins = 100)
#


#pd.plotting.scatter_matrix(data.all(),figsize=(10,10));

#plt.xlim(1.470e18,1.4705e18)
#plt.plot(data['Imon_change_date'].astype(np.int64),data['inst_lumi'],'.')   

#print(type(data['inst_lumi'][10]))
'''

'''
tans = []
times = []
for i in range(len(data)):
    if data['inst_lumi'][i] ==0: continue
    tan = (data['Imon'][i])/data['inst_lumi'][i]
    tans.append(tan)
    times.append(data['Imon_change_date'][i])
#plt.xlim(1.464e9,1.466e9)
plt.plot(times,np.log(tans))


print(max(tans))
plt.hist(np.log(tans),range=(-10,0), bins = 500)
print(tans)
#plt.xlim(0,10)
#plt.yscale('log')
#plt.xscale('log')


#plt.hist2d(data['inst_lumi'],data['Imon']-0.4,bins = 20)

#plt.hist(np.log(tans), range=(-11,-2), bins = 500)
#plt.show()
#overflowbin//
#cms tdr, rpc검출기 책 도서관\\\\
#inst_lumi에 대한 분포를 그려본다. 그 값이 0인거를 찾아서 그때의 Imon을 그리면 백그라운드가 나오겠지?
#그걸 Imon에서 빼주고 다시 그리면 더 정확한 그림이 나올것이다.




zero = []
for i in range(len(data)):
    if data['inst_lumi'][i] == 0:
        ze = data['Imon'][i]
        zero.append(ze)
#print(zero)
print(np.median(zero))
plt.hist2d(data['inst_lumi'],(data['Imon']-0.4),bins=25)

D = []
for i in range(len(data)):
    if type(data['uxc_change_date'][i]) == float:
        D.append(i)

print(len(D))

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
