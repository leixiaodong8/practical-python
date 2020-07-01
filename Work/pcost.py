# pcost.py
#
# Exercise 1.27

# importing sys to be able to read the script from the command line

import sys

def only_stocks(i): # function we will use later to return only floats and ints to the list
	try: 
		return int(i)
	except (ValueError, TypeError):
		try:
			return float(i)
		except (ValueError, TypeError):
			pass

def stock_price(file): # making a funciton because the file may vary

	total = 0 # variable to sum total
	stock_total = 1 # used to multiply values in the list

	# opening the file with a "with" statement so that it closes automatically
	# (although it is always good practice to also close the file manually)

	with open(file, "rt") as file:

		next(file) # skipping the first line

		for line in file: # iterating through the file
			print(line.strip("\n").split(",")) # visualizing original data
			stock_value = [only_stocks(e) for e in line.split(",")] # list comprehension to create a list of only ints and floats
			for e in stock_value: # iterating through the list
				try:
					stock_total *= e
					if isinstance(stock_total, float):
						print("Total stock value of this company is:", round(stock_total, 2), "\n") # visualizing each stock value separatly
						total += stock_total # summing values
				except TypeError: 	# because it is going to iterate through all elements, to prevent
					stock_total = 1 # the iteration to sum everything, the value resets at each None object (str)

		print("Your total is:", round(total, 2))

	# closing the file

	file.close()

	# enabling the code to be executed from the command line

	if len(sys.argv) == 2:
		file = sys.argv[1]



stock_price("Data/portfolio.csv")
