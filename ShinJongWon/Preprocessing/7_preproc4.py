import multiprocessing
import os
import pandas as pd
from datetime import datetime
import time



IN_PATH_2016 = "/Users/mainroot/RPC-test_data/cert_data/2016/"
IN_PATH_2017 = "/Users/mainroot/RPC-test_data/cert_data/2017/"
IN_PATH_2018 = "/Users/mainroot/RPC-test_data/cert_data/2018/"

OUT_PATH_2016 = "/Users/mainroot/RPC-test_data/cert_data/2016_final/"
OUT_PATH_2017 = "/Users/mainroot/RPC-test_data/cert_data/2017_final/"
OUT_PATH_2018 = "/Users/mainroot/RPC-test_data/cert_data/2018_final/"



def preprocessing(inputpath, filename, outputpath):
    data = pd.read_csv(inputpath + filename)
    is_certed = []

    for i in range(len(data)):
        Imon_time = data["Imon_change_date"][i]
        converter = datetime.strptime(Imon_time, "%Y-%m-%d %H:%M:%S")
        Imon_time_sec = time.mktime(converter.timetuple())

        run_start_time = data["start_time"][i]
        converter = datetime.strptime(run_start_time, "%Y-%m-%d %H:%M:%S")
        run_start_time_sec = time.mktime(converter.timetuple())

        cert_start = run_start_time_sec + int(data["cert_start_time"][i])
        cert_end = run_start_time_sec + int(data["cert_end_time"][i])

        if (Imon_time_sec >= cert_start) and (Imon_time_sec <= cert_end):
            is_certed.append(True)
        else:
            is_certed.append(False)

    certed_data = data[is_certed]
    certed_data.to_csv(outputpath + filename, index=False)

    


if __name__ == "__main__":
    
    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2016)
    pool.starmap(preprocessing, [(IN_PATH_2016, filename, OUT_PATH_2016) for filename in filelist])
    pool.close()
    pool.join()


    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2017)
    pool.starmap(preprocessing, [(IN_PATH_2017, filename, OUT_PATH_2017) for filename in filelist])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2018)
    pool.starmap(preprocessing, [(IN_PATH_2018, filename, OUT_PATH_2018) for filename in filelist])
    pool.close()
    pool.join()





