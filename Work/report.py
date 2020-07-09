# report.py
#
# Exercise 2.4

import csv

def portfolio(filename):

    # returns csv data in a list of tuples and returns total cost of portfolio

    portfolio = []
    total = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)

        # orginizing in a tuples list

        for row in rows:
        	holding = (row[0], int(row[1]), float(row[2]))
        	portfolio.append(holding)
        print(portfolio)

        # calculating total based on tuples

        for names, shares, price in portfolio:
        	total += shares * price
        print(total)


portfolio("Data/portfolio.csv")

def dict_portfolio(filename):

    # it returns the data in a dictionary form inside of a list
    # and also calculates the total cost of the portfolio

    portfolio_list = []
    portfolio = {}

    with open(filename, "rt") as file:
        rows = csv.reader(file)
        next(rows)

        # appending values to the list

        

        # calculating total with an iteration through the dictionaries

        for e in portfolio_list:
            total = 0.0
            total += e["shares"] * e["price"]
        print(total)

dict_portfolio("Data/portfolio.csv")


