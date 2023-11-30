""" Vi tilføjer en funktion __repr__ til vores klasse, så print() giver flottere resultater.

Kør programmet.
Læs alle kommentarerne.
Forstå programkoden. """

from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select

Database = 'sqlite:///S2206_my_first_sql_database.db'
Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Person({self.id=}    {self.name=}    {self.age=})"


def select_all(classparam):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # in the background this creates the sql query "select * from persons" when called with classparam=Person
        result = []
        for record in records:  # convert the query result into a list of records
            result.append(record)
    return result


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

print(select_all(Person))
