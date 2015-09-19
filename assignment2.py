import math
import datetime

class Customer(object):
	def __init__(self, name, idno,no_of_days, bag=[]):
		self.name=name
		self.idno=idno
		self.no_of_days =no_of_days
		self.bag=bag

class Movie(object):
	def __init__(self, movie_name, category, price):
		self.movie_name=movie_name
		self.category=category
		self.price=price

class Owner(object):
	def __init__(self, movie_lent=[], movie_returned=[], library=[], customer_list=[]):
		self.movie_lent=movie_lent
		self.movie_returned=movie_returned
		self.library=library
		self.customer_list=customer_list

bag = []
total_price =0
jane =Customer("Jane", 123, 2)
owner = Owner()
hitman =Movie("Hitman", "New Release", 1000)
frozen = Movie("Frozen", "Children's", 300)
tangled =Movie("Tangled", "Children's", 300)
inception =Movie("Inception", "Regular", 500)
phantom =Movie("Phantom", "New Release", 1000)
library = ["Hitman", "Tangled", "Frozen", "Inception", "Phantom"]
if __name__== "__main__":
	while True:
		choice =int(raw_input("1.Borrow a movie\n2.Return movie\nEnter choices [1-3] "))

		if choice ==1:
			print "\nCustomer Name: %s" %jane.name
			print "\n Customer ID: %r\n" %jane.idno
			print "\n No of days with movie: %r" %jane.no_of_days
			print "**LIST OF AVAILABLE MOVIES**"
			print library

			#remove from lib and add to the bag
			for movie in library:
				date_borrowed = datetime.date.today()
				date_returned = date_borrowed + datetime.timedelta(days=2)
				while True:

					if movie == "Phantom":
						library.remove(movie)
						bag.append(movie)
					elif movie == "Frozen":
						library.remove(movie)
						bag.append(movie)				
					elif movie == "Hitman":
						library.remove(movie)
						bag.append(movie)
					break
			print "\nMovies Chosen"
			print "\nMOVIE\t\tCATEGORY\t\tCATEGORY PRICE\t\t"
			print "%s\t\t%s\t\t%r" %(phantom.movie_name, phantom.category, phantom.price)
			print "%s\t\t%s\t\t%r" %(frozen.movie_name, frozen.category, frozen.price)
			print "%s\t\t%s\t\t%r" %(hitman.movie_name, hitman.category, hitman.price)

			
			total_price = phantom.price + frozen.price + hitman.price
			# print "INITIAL TOTAL: %s" %total_price
			discount =0.1
			discount_price = 0.1 * total_price
			print "\nDISCOUNT: %s" %discount_price
			new_total = (total_price - discount_price)* jane.no_of_days
			print "\nDISCOUNTED PRICE: %s" %new_total
			print "\n**MOVIES IN BAG**"
			print bag
			print "\n**AVAILABLE MOVIES IN LIBRARY**"
			print library

		elif choice == 2:
			print "Customer Name: %s" %jane.name
			print "No of days : %r" %jane.no_of_days
			for movie in bag:
				if movie == "Hitman":

					bag.remove(movie)
					library.append(movie)
					time_diff = abs((date_returned -date_borrowed).days) -jane.no_of_days
					if time_diff > jane.no_of_days:
						charge = 200 * time_diff
						fine = total_price + charge
						print "FINE: %s" %fine
				else:
					break 
			print "\nMOVIE\t\tCATEGORY\t\tCATEGORY PRICE\t\t\n"
			print "%s\t\t%s\t\t%r" %(hitman.movie_name, hitman.category, (hitman.price* jane.no_of_days))
			print "\nTOTAL CHARGE: %s\n" %(hitman.price* jane.no_of_days)
					
			

