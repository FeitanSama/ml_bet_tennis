from pymongo import MongoClient
import pandas as pd
import os

# client = MongoClient('localhost',27017)
client = MongoClient("mongodb+srv://guicha:guicha@projetdata.zity6.mongodb.net/?retryWrites=true&w=majority")
db = client.tennis

csv_prep_path = os.getcwd() + '/data/prep/prep.csv'

df = pd.read_csv(csv_prep_path)

db.atp.drop()

db.atp.insert_many(df.to_dict('records'))