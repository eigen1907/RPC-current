import multiprocessing
import os
import pandas as pd


path_2016 = "/Users/mainroot/RPC-test_data/2016/"
path_2017 = "/Users/mainroot/RPC-test_data/2017/"
path_2018 = "/Users/mainroot/RPC-test_data/2018/"

run_path_2016 = "/Users/mainroot/RPC-test_data/run_data/2016.csv"
run_path_2017 = "/Users/mainroot/RPC-test_data/run_data/2017.csv"
run_path_2018 = "/Users/mainroot/RPC-test_data/run_data/2018.csv"

outputPath_2016 = "/Users/mainroot/RPC-current/ShinJongWon/2016_addrun/"
outputPath_2017 = "/Users/mainroot/RPC-current/ShinJongWon/2017_addrun/"
outputPath_2018 = "/Users/mainroot/RPC-current/ShinJongWon/2018_addrun/"



def loopFunction(dataPath, filename, runData, outputPath):

    data = pd.read_csv(dataPath + filename)
    break_point = 0
    data["run_number"] = None
    data["fill_number"] = None
    data["run_start"] = None
    data["run_end"] = None
    for j in range(len(data)):
        for k in range(break_point, len(runData)):
            if data["Imon_change_date"][j] >= runData["start_time"][k] and data["Imon_change_date"][j] <= runData["end_time"][k]:
                data["run_number"][j] = runData["run_number"][k]
                data["fill_number"][j] = runData["fill_number"][k]
                data["run_start"][j] = runData["start_time"][k]
                data["run_end"][j] = runData["end_time"][k]
                break_point = k
                break

    data.to_csv(outputPath + filename, index=False)



if __name__ == "__main__":
    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    fileList = os.listdir(path_2017)
    runData = pd.read_csv(run_path_2017)
    pool.starmap(loopFunction, [(path_2017, filename, runData, outputPath_2017) for filename in fileList])
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(8)
    m = multiprocessing.Manager()
    fileList = os.listdir(path_2018)
    runData = pd.read_csv(run_path_2018)
    pool.starmap(loopFunction, [(path_2018, filename, runData, outputPath_2018) for filename in fileList])
    pool.close()
    pool.join()


