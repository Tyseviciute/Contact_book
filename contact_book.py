# AUTORIUS: Karina Tyševičiūtė

from sqlalchemy import Column, Integer, String, Date, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date

engine = create_engine("sqlite:///kontaktu_knyga.db")
Base = declarative_base()


class ContactBook(Base):
    __tablename__ = "contact_list"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lname = Column(String)
    bday = Column(Date)
    job = Column(String)
    phone_number = Column(Integer)
    email_adress = Column(String)
    created_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, lname, bday, job, phone_number, email_adress):
        self.name = name
        self.lname = lname
        self.bday = bday
        self.job = job
        self.phone_number = phone_number
        self.email_adress = email_adress

    def __repr__(self):
        return f"{self.id} {self.name} - {self.bday}, {self.job}, {self.phone_number}: {self.email_adress}"

Base.metadata.create_all(engine)
