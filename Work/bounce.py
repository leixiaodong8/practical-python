# bounce.py
#
# Exercise 1.5

# defining function so it works universaly with any number
def bounce(x):

	# defining initial list to be used in dict later
    bounce_list = [x]

    # running a "while" loop for the first 10 values of the bounce_list
    while len(bounce_list) <= 10:

    	# iterating through the results
        result = x * (3/5)
        x = result

        # appending the results to the bounce_list
        bounce_list.append(round(result, 4))

    # dictionary comprehension to create a dict with bounce_list and add key values to them
    data = {range(0, 11)[i]: bounce_list[i] for i in range(len(range(0, 11)))}
    print(data)

# calling the funciton
bounce(100)
