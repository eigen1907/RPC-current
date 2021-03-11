import multiprocessing
import os
import pandas as pd


IN_PATH_2016 = "/Users/mainroot/RPC-current/ShinJongWon/2016_addrun/"
IN_PATH_2017 = "/Users/mainroot/RPC-current/ShinJongWon/2017_addrun/"
IN_PATH_2018 = "/Users/mainroot/RPC-current/ShinJongWon/2018_addrun/"

OUT_PATH_2016 = "/Users/mainroot/RPC-current/ShinJongWon/2016_addrun2/"
OUT_PATH_2017 = "/Users/mainroot/RPC-current/ShinJongWon/2017_addrun2/"
OUT_PATH_2018 = "/Users/mainroot/RPC-current/ShinJongWon/2018_addrun2/"


def preprocessing(inputpath, filename, outputpath):
    data = pd.read_csv(inputpath + filename)
    data.dropna(how='any', inplace=True)
    data.to_csv(outputpath + filename)


if __name__ == "__main__":
    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2016)
    pool.starmap(preprocessing, [(IN_PATH_2016, filename, OUT_PATH_2016) for filename in filelist])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2017)
    pool.starmap(preprocessing, [(IN_PATH_2017, filename, OUT_PATH_2017) for filename in filelist])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    filelist = os.listdir(IN_PATH_2018)
    pool.starmap(preprocessing, [(IN_PATH_2018, filename, OUT_PATH_2018) for filename in filelist])
    pool.close()
    pool.join()
    