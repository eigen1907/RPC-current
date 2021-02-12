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
