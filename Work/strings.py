# exercises 1.13 to 1.18
#
# strings are read only, meaning that no modifications can be made to the string
# after atributing a certain variable to it

symbols = "AAPL,IBM,MSFT,YHOO,SCO"
print(symbols)

# Extracting individual characters and substrings:

print(symbols[0], symbols[1], symbols[2])
print(symbols[-1], symbols[-2]) # negative indexes reffer to the last values in an indexed object

# Stirng concatenation:
# what can be done, however, is reassign a variable to a newly created string
# destroying the old string in the process

symbols += ",GOOG"
symbols = "HPQ," + symbols
print(symbols)

# Membership testing: 

print("IBM" in symbols)
print("AA" in symbols)
print("CAT" in symbols)

# "AA" returns True because
# it is contained inside symbols as a part of a word

# String methods:

lower_syms = symbols.lower() # lowercase
print(lower_syms)

print(symbols.find("MSFT")) # returns the numerical position of the string part
print(symbols[13:17])

symbols = symbols.replace("SCO", "DOA")
print(symbols)

name = "         IBM       \n"
name = name.strip() # stripping the blankspace
print(name)

# f-strings:

name = "IBM"
shares = 100
price = 91.1
print(f"{shares} shares of {name} at ${price:0.2f}")

# Regular expressions:

text = "Today is 27/3/2018. Tomorrow is 28/3/2018."

# to find all the occurrences of a certain date we must use the re module

import re
print(re.findall(r"\d+/\d+/\d+", text))

# replacing all occurrences of a date with replacement text

new_text = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3/\2/\1", text)
print(new_text)

# to view supported operations, the dir() function might help

# print(dir(str)) or, in the interactive console, dir(str) will do
#
# to view more information about a specific command, the help()
# function might help
