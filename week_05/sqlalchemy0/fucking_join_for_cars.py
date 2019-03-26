import sqlalchemy as db
from pprint import pprint


from config import username
DATABASE_URI = f'postgres+psycopg2://{username}@localhost:5432/car_dealers'
engine = db.create_engine(DATABASE_URI)
connection = engine.connect()
metadata = db.MetaData()


users = db.Table('users', metadata, autoload=True, autoload_with=engine)
cars = db.Table('cars', metadata, autoload=True, autoload_with=engine)
users_cars = db.Table('users_cars', metadata, autoload=True, autoload_with=engine)


query = db.select([users, cars, users_cars])
selection = connection.execute(query).fetchall()


j = users.join(users_cars, users.user_id == users_cars.user_id)
