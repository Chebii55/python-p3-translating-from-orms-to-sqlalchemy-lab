from models import Dog
from sqlalchemy import (create_engine)

def create_table(base,engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs=session.query(Dog).all()
    return [dog for dog in dogs]

def find_by_name(session, name):
    dogs=session.query(Dog).filter(Dog.name.like(name)).all()
    
    for dog in dogs:
        return dog

    

def find_by_id(session, id):
    dogs=session.query(Dog).filter(Dog.id.like(id)).all()
    
    for dog in dogs:
        return dog

def find_by_name_and_breed(session, name, breed):
    dogs=session.query(Dog).filter(Dog.name.like(name),Dog.breed.like(breed)).all()
    
    for dog in dogs:
        return dog
    

def update_breed(session, dog, breed):
    x=session.query(Dog).filter(Dog.name.like(f'%{dog}%')).first()
    if dog:
        dog.breed = breed
        session.commit()
        return dog
    else:
        print(f"No dog found with name like {dog}")
        return None

