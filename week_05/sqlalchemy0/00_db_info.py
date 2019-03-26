'''

All of the following exercises should be done using sqlalchemy0.

Using the dvdrental schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy as db
from pprint import pprint
username = 'Blake'

URI = f'postgres+psycopg2://{username}@localhost:5432/dvdrental'
engine = db.create_engine(URI)
connection = engine.connect()
metadata = db.MetaData()
t1 = [db.Table('film_category', metadata, autoload=True, autoload_with=engine)]


query = db.select(t1)
selection = connection.execute(query).fetchall()
pprint(selection)


