from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.orm import sessionmaker
import csv
from datetime import datetime

ENGINE = None
Session = None

Base = declarative_base()

class Order(Base):
	__tablename__ = "orders"

	id = Column(Integer, primary_key = True)
	order_date = Column(Date)
	status = Column(String(30))
	customer_id = Column(Integer, nullable = False)
	email = Column(String(64))
	address = Column(String(64))
	city = Column(String(30))
	state = Column(String(5))
	postalcode = Column(String(15))
	num_watermelons = Column(Integer)
	num_othermelons = Column(Integer)
	subtotal = Column(Numeric(10,2))
	tax = Column(Numeric(10,2))
	order_total = Column(Numeric(10,2))

class Customer(Base):
	__tablename__ = "customers"

	id = Column(Integer, primary_key = True)
	first = Column(String(20))
	last = Column(String(20))
	email = Column(String(64))
	telephone = Column(String(20))
	called = Column(Date)

def connect():
	global ENGINE
	global Session

	ENGINE = create_engine("sqlite:///melons.db", echo=True)
	Session = sessionmaker(bind=ENGINE)

	return Session()

def create_database(session):
	global ENGINE
	Base.metadata.create_all(ENGINE)

def main():
	session = connect()
	# create_database(session)

if __name__ == "__main__":
	main()