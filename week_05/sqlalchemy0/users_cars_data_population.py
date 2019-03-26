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

query = db.insert(users_cars)

users_cars_data = [{'user_id': 1, 'car_id': 1},
    {'user_id': 2, 'car_id': 2},
    {'user_id': 3, 'car_id': 3},
    {'user_id': 4, 'car_id': 4},
    {'user_id': 5, 'car_id': 5}]

result_proxy = connection.execute(query, users_cars_data)

