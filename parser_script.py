import os

import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongodb_dns = os.getenv('MONGODB_DSN')
cluster = MongoClient(mongodb_dns)

db = cluster['excel']
users = db['users']
df = pd.read_excel('test.xlsx')
# users.insert_many(df.to_dict('records'))


print(users.find_one({'ИНН сотрудника': 720419401885}))