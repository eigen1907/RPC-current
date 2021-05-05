import json
import pandas as pd
import multiprocessing
import os




def joinRunInfo(rpcIMONFileName, runInfoFileName, certFileName, outFileName):
    timeOfLS = 23.3 ## 23.3seconds = 2^18 orbits, 1 orbit = 26.7km/(speed of light)

    ## Load the IMON data
    #print('='*80)
    #print("Loading RPC IMON info, '%s'" % rpcIMONFileName)
    rpcIMONs = pd.read_csv(rpcIMONFileName)

    #### convert dates stored in str formats to the native datetime format
    rpcIMONs = rpcIMONs.drop(columns=['Imon_change_date2'])
    for colName in ['Imon_change_date','lumi_start_date','lumi_end_date','uxc_change_date']:
        rpcIMONs[colName] = pd.to_datetime(rpcIMONs[colName])

    #print("  Number of total entries =", len(rpcIMONs))
    #print("  Invalid IMON change date =", len(rpcIMONs[rpcIMONs['Imon_change_date'] != rpcIMONs['Imon_change_date']]))
    #print("  IMON change before lumi starts =", len(rpcIMONs[rpcIMONs['lumi_start_date'] > rpcIMONs['Imon_change_date']]))
    #print("  IMON change after lumi ends    =", len(rpcIMONs[rpcIMONs['lumi_end_date'] < rpcIMONs['Imon_change_date']]))

    ## Load the run number information taken from the OMS
    #print('-'*80)
    #print("Loading run info, '%s'" % runInfoFileName)
    runsInfo = pd.read_csv(runInfoFileName)
    for colName in ['start_time','end_time']:
        runsInfo[colName] = pd.to_datetime(runsInfo[colName])

    #print("  Number of total entries =", len(runsInfo))
    #runsInfo = runsInfo[runInfo['hlt_key'].str.match('.*cdaq/physics/.*')] ## Select physics runs
    #print(runsInfo[~runsInfo['hlt_key'].str.match('.*cdaq/physics/.*')]['hlt_key'])
    runsInfo = runsInfo[runsInfo['l1_hlt_mode_stripped'].str.match('collisions.*')] ## Select physics runs
    #print("  Entries after collision run selection =", len(runsInfo))
    #print("  Number of unique fill numbers =", len(runsInfo['fill_number'].unique()))
    #print("  Number of unique run numbers  =", len(runsInfo['run_number'].unique()))
    #print('='*80)

    ## Next step is to filter out IMON data points which are not certified as good LS.
    ##   Note: we don't use pandas here since the format is not that trivial for the pandas
    ## Load the CMS JSON file for the data certification and loop over the good LS
    ## and collect matching runInfo & IMONs within the good LS ranges.
    selIMONs = []
    certJSON = json.load(open(certFileName))

    lenAll = 0
    for runNumber, lumis in certJSON.items():
        runNumber = int(runNumber)
        runInfo = runsInfo[runsInfo.run_number == runNumber]
        if len(runInfo) == 0: continue
        if len(runInfo) != 1: print("Warning: multiple runs in JSON, should not happen!!!")
        runInfo = runInfo.iloc[0]
        fillNumber = runInfo.fill_number


        t0 = runInfo['start_time']
        for l1, l2 in lumis:
            t1 = t0 + pd.Timedelta(timeOfLS*(l1-1), unit='sec')
            t2 = t0 + pd.Timedelta(timeOfLS*l2, unit='sec')
            selIMON = rpcIMONs[(rpcIMONs.Imon_change_date >= t1) & (rpcIMONs.Imon_change_date <= t2)]
            nSel = len(selIMON)
            if nSel == 0: continue
            selIMON = selIMON.assign(run_number=runNumber)
            selIMON = selIMON.assign(fill_number=fillNumber)
            selIMONs.append(selIMON)

    ## Join the runInfo & IMON dataframes to build the 'master' dataframe
    try:
        dfAll = pd.concat(selIMONs, ignore_index=True)
        dfAll.to_csv(outFileName, index=False)
    except:
        print(f"concat error, {rpcIMONFileName}")




if __name__ == "__main__":
    IN_PATH_2016 = "/Users/mainroot/RPC-test_data/original/2016/"
    IN_PATH_2017 = "/Users/mainroot/RPC-test_data/original/2017/"
    IN_PATH_2018 = "/Users/mainroot/RPC-test_data/original/2018/"

    RUN_INFO_FILE_2016 = "/Users/mainroot/RPC-test_data/run_data/collisions2016.csv"
    RUN_INFO_FILE_2017 = "/Users/mainroot/RPC-test_data/run_data/collisions2017.csv"
    RUN_INFO_FILE_2018 = "/Users/mainroot/RPC-test_data/run_data/collisions2018.csv"

    CERT_FILE_2016 = "/Users/mainroot/RPC-test_data/runCertification/2016_271036-284044.json"
    CERT_FILE_2017 = "/Users/mainroot/RPC-test_data/runCertification/2017_294927-306462.json"
    CERT_FILE_2018 = "/Users/mainroot/RPC-test_data/runCertification/2018_314472-325175.json"

    OUT_PATH_2016 = "/Users/mainroot/RPC-test_data/last/2016/"
    OUT_PATH_2017 = "/Users/mainroot/RPC-test_data/last/2017/"
    OUT_PATH_2018 = "/Users/mainroot/RPC-test_data/last/2018/"

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2016)
    pool.starmap(joinRunInfo, [(IN_PATH_2016 + filename, RUN_INFO_FILE_2016, CERT_FILE_2016, OUT_PATH_2016 + filename) for filename in filelist])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist= os.listdir(IN_PATH_2017)
    pool.starmap(joinRunInfo, [(IN_PATH_2017 + filename, RUN_INFO_FILE_2017, CERT_FILE_2017, OUT_PATH_2017 + filename) for filename in filelist])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist= os.listdir(IN_PATH_2018)
    pool.starmap(joinRunInfo, [(IN_PATH_2018 + filename, RUN_INFO_FILE_2018, CERT_FILE_2018, OUT_PATH_2018 + filename) for filename in filelist])
    pool.close()
    pool.join()



