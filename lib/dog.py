# dog.py
from models import Base, Dog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_dir = 'dog.db'
SQLITE_URL = f'sqlite:///{db_dir}'

def create_table(base, engine):
    base.metadata.create_all(engine)

def find_by_id(session, id):
    return session.get(Dog, id)

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

engine = create_engine(SQLITE_URL)
Session = sessionmaker(bind=engine)
session = Session()


create_table(Base, engine)

joey = Dog(name="joey", breed="cocker spaniel")
joey2 = Dog(name="joey2", breed="cocker spaniel")
save(session, joey)
save(session, joey2)

dogs = get_all(session)
for dog in dogs:
    print(dog.name, dog.breed)

found_dog = find_by_id(session, 1)
print(found_dog)

session.close()