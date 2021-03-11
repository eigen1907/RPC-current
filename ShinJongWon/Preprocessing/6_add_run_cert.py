import multiprocessing
import os
import pandas as pd


IN_PATH_2016 = "/Users/mainroot/RPC-test_data/addrun2/2016_addrun2/"
IN_PATH_2017 = "/Users/mainroot/RPC-test_data/addrun2/2017_addrun2/"
IN_PATH_2018 = "/Users/mainroot/RPC-test_data/addrun2/2018_addrun2/"


OUT_PATH_2016 = "/Users/mainroot/RPC-test_data/cert_data/2016/"
OUT_PATH_2017 = "/Users/mainroot/RPC-test_data/cert_data/2017/"
OUT_PATH_2018 = "/Users/mainroot/RPC-test_data/cert_data/2018/"


CERT_PATH_2016 = "/Users/mainroot/RPC-test_data/runCertification/cert_run2016.csv"
CERT_PATH_2017 = "/Users/mainroot/RPC-test_data/runCertification/cert_run2017.csv"
CERT_PATH_2018 = "/Users/mainroot/RPC-test_data/runCertification/cert_run2018.csv"



cert_data2016 = pd.read_csv(CERT_PATH_2016)
cert_data2017 = pd.read_csv(CERT_PATH_2017)
cert_data2018 = pd.read_csv(CERT_PATH_2018)



def merge_by_run(inputpath, filename, cert_file, outputpath):
    data = pd.read_csv(inputpath + filename)
    data = data.drop(columns="Unnamed: 0")
    data = data.astype({"run_number": "int", "fill_number": "int"})
    new_data = pd.merge(data, cert_file, on="run_number")
    new_data.to_csv(outputpath + filename, index=False)



if __name__ == "__main__":
    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2016)
    pool.starmap(merge_by_run, [(IN_PATH_2016, filename, cert_data2016, OUT_PATH_2016) for filename in filelist])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    filelist= os.listdir(IN_PATH_2017)
    pool.starmap(merge_by_run, [(IN_PATH_2017, filename, cert_data2017, OUT_PATH_2017) for filename in filelist])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(6)
    m = multiprocessing.Manager()
    filelist= os.listdir(IN_PATH_2018)
    pool.starmap(merge_by_run, [(IN_PATH_2018, filename, cert_data2018, OUT_PATH_2018) for filename in filelist])
    pool.close()
    pool.join()


