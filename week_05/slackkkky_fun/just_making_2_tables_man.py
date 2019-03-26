'''

Building on the example more_APIs/00_slack, make a new database with two tables to model this object:

{
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
}

Think about what tables are required to model this object. Do you need two tables? Three?

Now, instead of saving the list of these objects to a JSON file, persist the data
to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''
import sqlalchemy as db
from pprint import pprint


from config import username
DATABASE_URI = f'postgres+psycopg2://{username}@localhost:5432/slack'
engine = db.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = db.MetaData()

messages = db.Table('messages', metadata,
                    db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
                    db.Column('link', db.String(500), nullable=False),
                    db.Column('description', db.Text()),
                    db.Column('date_added', db.Integer()),
                    db.Column('read', db.Boolean, default=False),
                    db.Column('rating', db.Integer(), default=0),
                    db.Column('starred', db.Boolean(), default=False)
                    )

comments = db.Table('comments', metadata,
                    db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
                    db.Column('message_id', db.Integer(), db.ForeignKey('messages.id')),
                    db.Column('author', db.String(200), nullable=False),
                    db.Column('content', db.Text(), nullable=False))

metadata.create_all(engine)

#creating a test table
# test = sqa.Table('test', metadata,
#                  sqa.Column('id', sqa.Integer(), autoincrement=True, primary_key=True),
#                  sqa.Column('quote', String(255), nullable=False),
#                  )
# #the second column entry allows you to choose what you like quote or link
# metadata.create_all(engine)