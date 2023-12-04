from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select

Database = 'sqlite:///S2311_cool_database.db'  # first part: database type, second part: file path
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    contact = Column(String)

    def __repr__(self):
        return f"id: {self.id}, last name: {self.last_name}, contact: {self.contact}"

    def to_tuple(self):
        return (self.id, self.last_name, self.contact)


class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True)
    start_end = Column(String)
    date = Column(String)
    capacity = Column(Integer)


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    route_id = Column(Integer)
    seats = Column(Integer)


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

def create_costumer(_last_name, _contact):
    with Session(engine) as session:
        new_costumer = Customer(last_name = _last_name, contact = _contact)
        session.add(new_costumer)
        session.commit()

def delete_costumer(id):
    pass

def update_costumer(id, _last_name, _contact):
    pass

def update_costumer(id, _last_name):
    pass

def update_costumer(id, _contact):
    pass

def read_all_customers():
    return select_all(Customer)

engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_costumer("testjohn", "contact@john.com")
create_costumer("testjohn2", "contact@2john.com")
create_costumer("testjohn3", "contact@3john.com")

print(get_record(Customer, 0))
print(get_record(Customer, 1))
print(get_record(Customer, 2))
print(get_record(Customer, 1))


