from entities.person_entity import Person, db

def create_person(name, email):
    person = Person(name=name, email=email)
    db.session.add(person)
    db.session.commit()
    return person

def get_all_people():
    return Person.query.all()

def get_person_by_id(person_id):
    return Person.query.get(person_id)

def update_person(person_id, name, email):
    person = Person.query.get(person_id)
    if person:
        person.name = name
        person.email = email
        db.session.commit()
        return person
    return None

def delete_person(person_id):
    person = Person.query.get(person_id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return True
    return False