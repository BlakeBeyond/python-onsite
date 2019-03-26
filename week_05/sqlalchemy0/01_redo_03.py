'''
Redo the exercises from '03_pgadmin.txt' in the SQL labs using SQLAlchemy .
- create a new table named "users_cars" with the following fields:
    - id (auto increment)
    - userID (refers to "id" in users table)
    - carID (refers to "id" in cars table)
'''
import sqlalchemy as db
from pprint import pprint


from config import username
DATABASE_URI = f'postgres+psycopg2://{username}@localhost:5432/car_dealers'
engine = db.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = db.MetaData()

users_cars = db.Table('users_cars', metadata,
                    db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
                    db.Column('user_id', db.Integer()),
                    db.Column('car_id', db.Integer()))

users = db.Table('users', metadata,
                    db.Column('user_id', db.Integer(), autoincrement=True, primary_key=True),
                    #db.Column('user_id', db.Integer(), db.ForeignKey('users_cars.user_id')),
                    db.Column('first_name', db.Text()),
                    db.Column('last_name', db.Text()))

cars = db.Table('cars', metadata,
                db.Column('car_id', db.Integer(), autoincrement=True, primary_key=True),
                #db.Column('car_id', db.Integer(), db.ForeignKey('users_cars.car_id')),
                db.Column('make', db.Text()),
                db.Column('model', db.Text()),
                db.Column('color', db.Text()),
                db.Column('year', db.Integer()))

#metadata.create_all(engine)

#query = db.insert(cars)

users_data = [{'first_name': 'Fredrik', 'last_name': 'Hossak'},
    {'first_name': 'Daniel', 'last_name': 'Wankmann'},
    {'first_name': 'Andreas', 'last_name': 'Kovacs'},
    {'first_name': 'Blake', 'last_name': 'Lezenski'},
    {'first_name': 'Mr', 'last_name': 'Martin'}]

# result_proxy = connection = connection.execute(query, users_data)

cars_data = [{'make': 'Mercedes', 'model': 'SL', 'color': 'black', 'year': '1988'},
{'make': 'Suzuki', 'model': 'SX4', 'color': 'red', 'year': '2011'},
{'make': 'Toyota', 'model': 'Yaris', 'color': 'silver', 'year': '2008'},
{'make': 'Dodge', 'model': 'Charger', 'color': 'Green', 'year': '1966'},
{'make': 'Toyota', 'model': 'Corolla', 'color': 'white', 'year': '2001'}]

#result_proxy = connection = connection.execute(query, cars_data)

# t1 = [db.Table('users', metadata, autoload=True, autoload_with=engine)]
#
#
# query = db.select(t1)
# selection = connection.execute(query).fetchall()
# pprint(selection)

# t2 = [db.Table('cars', metadata, autoload=True, autoload_with=engine)]
# query = db.select([cars]).where(cars.columns.make == 'Toyota')
# filtered = connection.execute(query).fetchall()
# pprint(filtered)

query = db.insert('users_cars')

users_cars_data = [{'user_id': 1, 'car_id': 1},
    {'user_id': 2, 'car_id': 2},
    {'user_id': 3, 'car_id': 3},
    {'user_id': 4, 'car_id': 4},
    {'user_id': 5, 'car_id': 5}]

result_proxy = connection = connection.execute(query, users_cars_data)

#query = session.db.query([users]).join(users_cars)

'''








     - use a join to select the first name and car model of every user who has bought a car

    - use a join to select the first and last name of everyone who has bought a red car


    - use an insert statement to create a new record in each table

     - use sql to update a record in the "cars" table

    - delete one record from the database
'''

# import sqlalchemy as db
# from pprint import pprint
# username = 'Blake'
#
# URI = f'postgres+psycopg2://{username}@localhost:5432/dvdrental'
# engine = db.create_engine(URI)
# connection = engine.connect()
# metadata = db.MetaData()
# t1 = [db.Table('film_category', metadata, autoload=True, autoload_with=engine)]

