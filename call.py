"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import seed
from sqlalchemy import and_, or_
from datetime import datetime, timedelta


# Retrieve the next uncontacted customer record from the database.
# Return the data in a Customer class object.
#
# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 melons or more.
def get_next_customer(session):
	eligible_orders = session.query(seed.Order).filter(seed.Order.num_watermelons >= "20").group_by(seed.Order.email).all()
	
	emails = []
	for order in eligible_orders:
		emails.append(order.email)

	now = datetime.date(datetime.now() - timedelta(days=30))
	customer = session.query(seed.Customer).filter(and_(seed.Customer.email.in_(emails), (or_(seed.Customer.called == None, seed.Customer.called < now)))).first()

	return customer


def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer.first, customer.last
	print customer.telephone
	print "Last called: ", customer.called
	print "\n"

# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer, session):
	customer.called = datetime.now()
	session.add(customer)
	session.commit()

def main():
	session = seed.connect()
	customer = get_next_customer(session)
	display_next_to_call(customer)

	update = raw_input("Update database? Y or N: ")
	if update == "Y":
		update_customer_called(customer, session)


if __name__ == '__main__':
	main()