# exercises 1.19 to 1.25
#
# defining string data

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

# making a list by spliting the string in all "," occurrences

sym_list = symbols.split(",")
print(sym_list)

# Extracting and reassigning list elements:

print("specific values: ", sym_list[0], sym_list[1], sym_list[-1], sym_list[-2])

sym_list[2] = "AIG" # redefining value located in index 2
print("redefined value at index [2]:", sym_list)

print(sym_list[0:3]) # slicing to extract values in a specific index range
print(sym_list[-2:]) # this will slice only the values up to the point specified

# creating a new list and assigning values to it

mylist = []
mylist.append("GOOG")
print(mylist)

# reassigning a portion of a list to another list
# the list on the left-hand-side will be resized according to the list in the right-hand-side

sym_list[-2:] = mylist
print(sym_list)

# Looping over list items:

for s in sym_list:
	print("s =", s)

# Membership testing:

print("AIG" in sym_list)
print("AA" in sym_list) # this returns False because now it's not looking specifaclly to a string, but a list item
print("CAT" not in sym_list)

# Appending, inserting and deleting items:

sym_list.append("RHT") # adds to the end of the list, last index
print(sym_list)

sym_list.insert(1, "AA") # inserting "AA" as the second value in the list
print(sym_list)

sym_list.remove("MSFT")
print(sym_list)

# working with duplicates

sym_list.append("YHOO")
print(sym_list)
print(sym_list.index("YHOO")) # this will only return the index of the first occurrence of a duplicate
print(sym_list.count("YHOO")) # counting how many times this value appears in the list

# there are two methods to remove a specific value from a list

sym_list.remove("YHOO") # this will remove the first occurrence of this value inside the list
# or
# del sym_list[index_number] # this will remove the specified index number
print(sym_list)

# Sorting:
#
# sorting is used to organize a list in a certain way,
# being in a numerical or alphabetical order
# no new list is created in this process,
# the values are only reorganized in the inteded way

sym_list. sort() # this will organize the list in alphabetical order
print(sym_list)
sym_list.sort(reverse = True) # this will reverse the alphabetical order
print(sym_list)

# Putting it all back together:
#
# joining a list of strings into a single string value

a = ",".join(sym_list) # this will join the list values with a "," separating them
print(a)
b = ":".join(sym_list) # this will join the list values with a ":" separating them
print(b)
c = "".join(sym_list) # this will join the list values without separations
print(c)

# Lists of anything:
#
# lists can contain any value, including other lists

nums = [101, 102, 103]
items = ["spam", sym_list, nums]
print(items)

# to access items inside a nested list, multiple index operations have to be used

print(items[0])
print(items[0][0])
print(items[1])
print(items[1][1])
print(items[1][1][2])
print(items[2])
print(items[2][1])
