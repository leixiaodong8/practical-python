# mortgage.py
#
# Exercise 1.7

# values

init_total = 5e5 # = 5 * (10 ** 5)
interest_rt = 5/100 # 5% per year, so it should be divided by 12 since it's a monthly pay
mon_pay = 2684.11

# we'll have to use compound interest in a while loop
# to calculate the total ammount

# setting variables to use in the while loops
# when a variable = 0 in a while loop it is used to add/iterate over elements

total = 0

# original while loop if Dave doesn't add extra payments

while init_total > 0:

	init_total = init_total * (1 + interest_rt/12) - mon_pay
	total += mon_pay

print("total without extra payments:", round(total, 2)) # rounding to clean it up
print("\n")

# redefining values to use in the other while loops

init_total = 5e5
interest_rt = 5/100
mon_pay = 2684.11
year1_extra_pay = mon_pay + 1000
total = 0
n_months = 0 # now the number of months matter

# if Dave only adds $1000 extra per month in the first year 

while init_total > 0:

	# paying extra 1000 in the first year

	if n_months < 12:
		init_total = init_total * (1 + interest_rt/12) - year1_extra_pay
		total += year1_extra_pay
		n_months += 1
		
	else:
		init_total = init_total * (1 + interest_rt/12) - mon_pay
		total += mon_pay
		n_months += 1

print(f"total of months: {n_months}, ", f"total with $1000 extra in first month: {round(total, 2)}")
print("\n")

# redefining values to use in the other while loops

init_total = 5e5
interest_rt = 5/100
mon_pay = 2684.11
year1_extra_pay = mon_pay + 1000
extra_start_mon = 61 # extra payments each start and end of month
extra_end_mon = 108
extra_mon_pays = extra_start_mon + extra_end_mon
total = 0
n_months = 0

# if Dave adds $1000/month in first year + start and end of months payments every month

while init_total > 0:

	if n_months < 12:
		init_total = init_total * (1 + interest_rt/12) - (year1_extra_pay + extra_mon_pays)
		total += (year1_extra_pay + extra_mon_pays)
		n_months += 1
		
	else:
		init_total = init_total * (1 + interest_rt/12) - (mon_pay + extra_mon_pays)
		total += (mon_pay + extra_mon_pays)
		n_months += 1

print(f"total of months: {n_months}, ", f"total with extra pay in first year and monthly pays: {round(total, 2)}")
print("\n")

# redefining values to use in the other while loops

init_total = 5e5
interest_rt = 5/100
mon_pay = 2684.11
year5_extra_pay = mon_pay + 1000 # extra payment now starts at year 5
extra_start_mon = 61
extra_end_mon = 108
extra_mon_pays = extra_start_mon + extra_end_mon
total = 0
n_months = 0

# if Dave adds $1000/month for 4 years starting at year 5
# + start and end of months payments every month

while init_total > 0:

	if (12 * 5) < n_months <= (12 * 9): # start of extra payment at year 5 and end in year 9
		init_total = init_total * (1 + interest_rt/12) - year5_extra_pay
		total += year5_extra_pay
		n_months += 1
		
	else:
		init_total = init_total * (1 + interest_rt/12) - mon_pay
		total += mon_pay
		n_months += 1

	# correcting overpayment on last month

	if init_total < mon_pay:
		mon_pay = init_total * (1 + interest_rt/12)
		init_total = init_total * (1 + interest_rt/12) - mon_pay
		n_months += 1

	print(n_months, round(total, 2), round(init_total, 2))

print(f"total of months: {n_months}, ", f"total with extra payment through 4th to 9th year: {round(total, 2)}")
