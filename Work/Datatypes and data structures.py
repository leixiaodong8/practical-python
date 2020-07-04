# this module discusses datatypes and data structures
#
# class 2.1
#
# None type:
#
# None is often used as a placeholder for optional or missing values
# they can also be used as a False statement, as seen in the example below

email_addr = None
if email_addr: # if False:
	send_email(email_addr, msg)

# Tuples:
#
# a tuple is a collection of values grouped together
# tipically, it is a single object of multiple parts
# i.g. (name of company, ammount of stocks, total price of the stocks)

s = ("GOOG", 100, 490.1)

# sometimes the () are ommited in the syntax

s = "GOOG", 100, 490.1

# they are ordered like an array or list
# but values cannot be modified

print(s[0])
print(s[1])
print(s[2])

# s[1] = 75 # would show an error saying "obj does not support item assignment"

# what can be done to "solve" this issue is 
# create a new tuple based on values of the original object

s = (s[0], 75, s[2])

# tuples can also be empty or have only one value

t = () # empty tuple
w = ("GOOG",) # one item tuple

# Tuple packing:
#
# Tuples are about packing related items together into a single object
# so that they can be more easily handled in other parts of the program

# Tuple unpacking:
#
# to use the tuple elsewhere, its parts can be divided and unpacked

name, shares, price = s # this gives the values inside the tuple
print(s)				# specific names to work with ("GOOG" = name, shares = 100, ...)

print("Cost:", shares * price) # here we are accessing the values by their names

# the number of names must match the tuple structure

# name, shares = s # would throw an error because the third value is still undefined

# Tupls vs. Lists:
#
# lists are usually a collection of distinct items of the same type
# i.g. names of companies or ammount of shares ["GOOGLE", "AMAZON", "IBM"]
#
# tuples, however, are most often used for a single item consisting of multiple parts
# i.g the ammount of shares and total value by company ("GOOGLE", 100, 490.1)

# Dictionaries:
#
# A dictionary (or hash table / associative array) consist of keys and values
# The keys serve as indices for accessing values

s = {
    "name": "GOOG",
    "shares": 100,
    "price": 490.1
}

# getting values from dictionaries by accessing the keys

print(s["name"], s["shares"], s["price"])

# modifying values assigned to keys

s["shares"] = 75

# new values can also be added

s["date"] = "06/06/2020"

# deleting values

del s["date"]

# dictionaries are useful when handling large ammounts of data
# that have many different values, while making the code more readable
# than tuples or lists and enabling modifications, making it more flexible

# Exercices:
#
# tuples

t = "GOOG", 100, 400.01

name, shares, price = t
print(t)

t = (name, 2*shares, price) # operations can be easily done inside tuples
print(t)

# dictionaries as a data structure

d = {
	"name": "GOOG",
	"shares": 100,
	"price": 400.01
}

print(d)

# operations can also be performed with dictionary keys
# that represent a certain value

cost = d["shares"] * d["price"]
print(cost)

# adding new elements and shifting existing ones

d["shares"] = 75 # this will change the outcome of the "cost" variable
print(d, cost)

d["account"] = 12345
d["date"] = "06/06/2020"
print(d)

# Additional dictionary operations:
#
# when turning a dictionary to list, the outcome will only account for the keys

dict_list = list(d)
print(dict_list)

# when iterating through a dictionary with a "for" loop, only keys will show up

for key in d:
	print("key =", key)

# a slight modification of this "for" loop will be able to access the values

for key in d:
	print("value =", d[key])

# to obtain all of the keys, the keys() function can also be used
# this function calls a specific object called dict_keys (a tuple)
# that always shows the current keys, even if the keys() function is not called again

keys = d.keys()
print(keys)
del d["account"]
print(keys) # the "account" key disappears

# to get simultaneously key and value pairs, the items() funciton can be used
# if a variable is assigned to d.items(), it functions in a similar way to d.keys()
# returning a specific object called dict_items (also a tuple)

pairs = d.items()
for key, value in pairs: # simply d.items() can also be used
	print(f"{key} = {value}")

# a dictionary can also be created from a tuple

print(pairs)
new_dict = dict(pairs)
print(new_dict)
