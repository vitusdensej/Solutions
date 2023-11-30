"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select

Database = 'sqlite:///S2311_my_second_sql_database.db'  # first part: database type, second part: file path
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    #def __init__(self, _id, _name, _address, _age):
    #    self.id = _id
    #    self.name = _name
    #    self.address = _address
    #    self.age = _age

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, address: {self.address}, age: {self.age}"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Integer)
    brand = Column(String)

    #def __init__(self):
    #    pass

    def __repr__(self):
        return f"id: {self.id}, product number: {self.product_number}, price: {self.price}, brand: {self.brand}"

def create_test_data():
    with Session(engine) as session:
        new_items = []

        new_items.append(Customer(name="John", address="sej gade 123", age=50))
        new_items.append(Customer(name="Ditte", address="en gade 456", age=30))
        new_items.append(Customer(name="Pernille", address="et sted 0x3940", age=66))
        new_items.append(Customer(name="Uli", address="en anden sej gade 987", age=3))
        new_items.append(Customer(name="Klement", address="et sted 576", age=55))

        new_items.append(Product(product_number=5069, price=1000, brand="sejt brand"))
        new_items.append(Product(product_number=69, price=2000, brand="det andet seje brand"))
        new_items.append(Product(product_number=420, price=3300, brand="brand06"))
        new_items.append(Product(product_number=3772, price=4065, brand="h&m"))

        session.add_all(new_items)
        session.commit()


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


def print_data():
    print("==== Customers ====")
    records = select_all(Customer)
    for r in records:
        print(r)
    print("==== Products ====")
    products = select_all(Product)
    for p in products:
        print(p)


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)


create_test_data()
print_data()
