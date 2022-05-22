import os
import glob
import pandas as pd

csv_source_path = os.getcwd() + '/data/raw'
csv_aggregate_path = os.getcwd() + '/data/aggr'

os.chdir(csv_source_path)
csv_list = glob.glob('*.{}'.format('csv'))

li=[]

for filename in csv_list:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv(csv_aggregate_path+'/aggr.csv')