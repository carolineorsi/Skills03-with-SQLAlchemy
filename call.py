"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import seed


# Retrieve the next uncontacted customer record from the database.
# Return the data in a Customer class object.
#
# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 melons or more.
def get_next_customer():
	eligible = session.query(seed.Order).filter(Order.num_watermelons >= 20).all()
	
	SELECT email FROM orders WHERE SUM(num_watermelons) > 20 GROUP BY email

	#customer = session.query(seed.Customer).filter_by().one()

	return customer


def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer
	print "\n"


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer):
	pass

def main():
	session = seed.Session()

	# connect_to_db()

	# done = False

	# while not done:
	# 	customer = get_next_customer()
	# 	display_next_to_call(customer)

	# 	print "Mark this customer as called?"
	# 	user_answer = raw_input('(y/n) > ')

	# 	if user_answer.lower() == 'y':
	# 		update_customer_called(customer)
	# 	else:
	# 		done = True


if __name__ == '__main__':
	main()