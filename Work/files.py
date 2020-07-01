# exercises 1.26 to 1.28

# File preliminaries:

with open("Data/portfolio.csv", "rt") as f: # the with statement is just used for good practice
	data = f.read()							# in case we forget to close the file
print(data) # in a command shell, this would give us the raw data
			# to prevent that, we may want to use a "for" loop to read the file line by line

with open("Data/portfolio.csv", "rt") as f: # "rt" means reading and "wt" means writing
	for line in f:
		print(line, end = "") # this will give us a line by line data that looks nicer

print("\n")

# to skip a specific line, the next() function can be used
# next() skips over the next line of text
# if it's called repeatedly, it will skip over the ammount of lines it is called
# however, the "for" loop already uses the next() function to iterate through lines

f = open("Data/portfolio.csv", "rt")
headers = next(f) # this will skip the first line
for line in f:
	print(line, end = "") # end = "" simply means that no "\n" is printed between each line
f.close()

print("\n")

# the data can also be put in a list through the splitting method

f = open("Data/portfolio.csv", "rt")
headers = next(f).split(",")
for line in f:
	row = line.strip("\n").split(",") # splits the data in all "," occurrences and puts it in a list
	print(row)						  # the .strip("\n") is for making the data a little bit neater
f.close() # the f.close() function is being called explicitly
		  # because the "with" statement is not being used

print("\n")

# Reading a data file:
#
# solution on file pcost.py

# Other kinds of "files":
#
# to read a non-text file such as a gzip or other compressed files,
# a built-in python module called gzip has to be used (Pandas can also be used)

import gzip

with gzip.open("Data/portfolio.csv.gz", "rt") as f:
	for line in f:
		print(line, end = "") 
