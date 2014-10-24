import seed
import csv
from datetime import datetime

def load_orders(session):
	f = open("orders.csv", "r")
	f.readline()
	data = csv.reader(f, delimiter=",")
	orders_list = []
	i = 0

	for row in data:
		order = seed.Order()
		order.id = row[0]
		order.order_date = datetime.strptime(row[1], "%m/%d/%Y")
		order.status = row[2].decode("latin-1")
		order.customer_id = row[3]
		order.email = row[4].decode("latin-1")
		order.address = row[5].decode("latin-1")
		order.city = row[6].decode("latin-1")
		order.state = row[7]
		order.postalcode = row[8]
		order.num_watermelons = row[9]
		order.num_othermelons = row[10]
		order.subtotal = row[11]
		order.tax = row[12]
		order.order_total = row[13]
		
		orders_list.append(order)	
		session.add(orders_list[i])
		i += 1


def load_customers(session):
	f = open("customers.csv")
	f.readline()
	data = csv.reader(f, delimiter=",")
	customers_list = []
	i = 0

	for row in data:
		customer = seed.Customer()
		customer.id = row[0]
		customer.first = row[1].decode("latin-1")
		customer.last = row[2].decode("latin-1")
		customer.email = row[3].decode("latin-1")
		customer.telephone = row[4]
		try:
			customer.called = datetime.strptime(row[5], "%m/%d/%Y")
		except:
			customer.called = None

		customers_list.append(customer)
		session.add(customers_list[i])
		i += 1

def main():
	session = seed.connect()
	load_orders(session)
	load_customers(session)
	#session.commit()

if __name__ == "__main__":
	main()