import pandas as pd


def dataFromPath(path):


  dataset = pd.read_csv(
    str(path),
    converters={i: str for i in range(0, 12)},
    header=None
  )


  dataset.columns = [
    'Imon_change_date',
    'Imon', 
    'Vmon', 
    'inst_lumi', 
    'lumi_start_date', 
    'lumi_end_date', 
    'Imon_change_date2', 
    'uxc_change_date', 
    'temp',
    'press', 
    'relative_humodity', 
    'dew_point'
  ]


  dataset = dataset.dropna()

  dataset['Imon_change_date'] = pd.to_datetime(dataset['Imon_change_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
  dataset['lumi_start_date'] = pd.to_datetime(dataset['lumi_start_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
  dataset['lumi_end_date'] = pd.to_datetime(dataset['lumi_end_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
  dataset['Imon_change_date2'] = pd.to_datetime(dataset['Imon_change_date2'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
  dataset['uxc_change_date'] = pd.to_datetime(dataset['uxc_change_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
  
  
  dataset['Imon'] = pd.to_numeric(dataset['Imon'], errors='coerce', downcast='float')
  dataset['Vmon'] = pd.to_numeric(dataset['Vmon'], errors='coerce', downcast='float')
  dataset['inst_lumi'] = pd.to_numeric(dataset['inst_lumi'], errors='coerce', downcast='float')
  dataset['temp'] = pd.to_numeric(dataset['temp'], errors='coerce', downcast='float')
  dataset['press'] = pd.to_numeric(dataset['press'], errors='coerce', downcast='float')
  dataset['relative_humodity'] = pd.to_numeric(dataset['relative_humodity'], errors='coerce', downcast='float')
  dataset['dew_point'] = pd.to_numeric(dataset['dew_point'], errors='coerce', downcast='float')
  

  dataset = dataset.dropna()


  return dataset



def dataFromPath2(path):


  dataset = pd.read_csv(
    str(path),
    converters={i: str for i in range(0, 11)},
    header=None
  )


  dataset.columns = [
    "run_number",
    "fill_number",
    "duration",
    "start_time",
    "end_time",
    "delivered_lumi",
    "recorded_lumi",
    "l1_triggers_counter",
    "l1_hlt_mode_stripped",
    "hlt_key",
    "initial_prescale_index"
  ]


  dataset = dataset.dropna()

  dataset["start_time"] = pd.to_datetime(dataset[ "start_time"], format='%Y-%m-%d %H:%M:%S', errors='coerce')
  dataset["end_time"] = pd.to_datetime(dataset["end_time"], format='%Y-%m-%d %H:%M:%S', errors='coerce')
  dataset["run_number"] = pd.to_numeric(dataset["run_number"], errors='coerce', downcast='integer')
  dataset["fill_number"] = pd.to_numeric(dataset["fill_number"], errors='coerce', downcast='integer')
  dataset["duration"] = pd.to_numeric(dataset["duration"], errors='coerce', downcast='integer')
  dataset["delivered_lumi"] = pd.to_numeric(dataset["delivered_lumi"], errors='coerce', downcast='float')
  dataset["recorded_lumi"] = pd.to_numeric(dataset["recorded_lumi"], errors='coerce', downcast='float')
  dataset["l1_triggers_counter"] = pd.to_numeric(dataset["l1_triggers_counter"], errors='coerce', downcast='integer')
  dataset["initial_prescale_index"] = pd.to_numeric(dataset["initial_prescale_index"], errors='coerce', downcast='integer')
  

  dataset = dataset.dropna()


  return dataset