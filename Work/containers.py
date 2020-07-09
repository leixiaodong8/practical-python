# class 2.2

# Lists as a container:
#
# lists are generally used when the order
# in which the data is stored matters,
# and can hold any type of object, such as tuples

portfolio = [
	("GOOG", 100, 490.01),
	("IBM", 50, 91.3),
    ("CAT", 150, 83.44)
]

portfolio[0] # = ("GOOG", 100, 490.01)
portfolio[1] # = ("IBM", 50, 91.3)

# List construction:
#
# building a list from an originally empty one
# using the .append() function
# (this can also be used while iterating through data)

records = []
records.append(("GOOG", 100, 490.01))
records.append(("IBM", 50, 91.3))
# the list now cointains the two tuples specified

# Dictionaries as containers:
#
# because they are unordered, dicitonaries are useful when
# the objective is to make a quick and random dataset where
# the order doesn't matter

prices = {
	"GOOG": 490.01,
	"IBM": 91.3,
	"CAT": 87.22
}

# Dictionary construction:
#
# building a dictionary from an originally empty one
# by just inserting new values with the assigned key

prices = {} 
prices["GOOG"] = 490.01
prices["IBM"] = 91.3
prices["CAT"] = 87.22

# building a dictionary from the Data/prices.csv file

prices = {}
with open('Data/prices.csv', 'rt') as f:
    try:
    	for line in f:
       		row = line.split(',')
       		prices[row[0]] = float(row[1]) # defining the dictionary values
    except IndexError: # accounting for the error in the last line
       	pass

print(prices)

# Dictionary lookups:
#
# the existance of a key in a dictionary can be checked

if '"CAT"' in prices:
	print("YES")
else:
	print("NO")

# if a key doesn't exist, a default value can be provided
# to check its existance

exists = prices.get('"IBM"', 0.0)
print(exists) # will return the key value of 106.28, because 
			  # it could retrieve a value
not_exists = prices.get('"SCOX"', 0.0)
print(not_exists) # will return 0.0, because it didn't find anything

# Composite keys:
#
# dictionaries can have as a key only immutable objects, such as tuples
# mutable ones are not accepted, such as lists, sets, and other dictionaries

holydays = {
	(1, 1): "New Years",
	(25, 12): "Christmas"
}

print(holydays[1, 1]) # to call a key tuple, all of its values have to be included

# Sets:
#
# sets are collections of unorded and unique data, but different
# to dictionaries, they do not have key value pairs, only values

tech_stocks = {"IBM", "AAPL", "MSFT"}
# or in an alternative syntax
tech_stocks = set(["IBM", "AAPL", "MSFT"])
print(tech_stocks)

# sets are useful for membership testing and eliminating duplicates

print("IBM" in tech_stocks) # memebership testing
print("FB" in tech_stocks)

names = ["GOOG", "IBM", "YHOO", "IBM", "GOOG"]
unique_names = set(names)
print(unique_names) # this will discard the first instance of the duplicate
					# ("YHOO" will be the first item)

# operations can also be performed in sets, such as .add() and .remove()
# | to unite two sets, & to add only the intersection of two sets and - to
# add only the difference of two sets 

unique_names.add("CAT")
unique_names.remove("CAT")

set1 = set(["this", "is", "set", "1"])
set2 = set(["this", "is", "set", "2"])
union = set1 | set2 
intersection = set1 & set2
difference = set1 - set2
# will give the output unordered, given that it is a set

print(union, intersection, difference)

# Exercises
#
# 2.4 - A list of tuples:
#
# solution in report.py file
#
# 2.5 - List of dictionaries:
#
# solution in report.py
#
#
