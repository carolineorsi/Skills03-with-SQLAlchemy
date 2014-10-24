"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import seed
from sqlalchemy import and_


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

	customer = session.query(seed.Customer).filter(and_(seed.Customer.email.in_(emails), seed.Customer.called == None)).first()

	return customer


def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer.first, customer.last
	print customer.telephone
	print "\n"


# def update_database(customer):

# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer):
	pass

def main():
	session = seed.connect()
	customer = get_next_customer(session)
	display_next_to_call(customer)

	# update = raw_input("Update database? Y or N: ")
	# if update == "Y":
	# 	update_database(customer)


if __name__ == '__main__':
	main()