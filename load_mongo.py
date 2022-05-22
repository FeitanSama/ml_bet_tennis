from pymongo import MongoClient
import pandas as pd
import os

client = MongoClient('localhost',27017)
db = client.tennis

df = pd.read_csv(os.getcwd()+'/aggr_1968-2022.csv')

db.atp.drop()

db.atp.insert_many(df.to_dict('records'))