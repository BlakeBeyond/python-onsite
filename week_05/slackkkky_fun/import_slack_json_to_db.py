import sqlalchemy as db
import json
from pprint import pprint


from config import username
DATABASE_URI = f'postgres+psycopg2://{username}@localhost:5432/slack'
engine = db.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = db.MetaData()

messages = db.Table('messages', metadata, autoload=True, autoload_with=engine)
with open('slack_data.json','r' ) as my_data:
    list_of_dic = json.load(my_data)


for msg in list_of_dic:
    if 'comments' in msg:
        del msg['comments']

for msg in list_of_dic:
    if 'description' not in msg:
        msg['description'] = "None"

query = db.insert(messages)
connection.execute(query, list_of_dic)

