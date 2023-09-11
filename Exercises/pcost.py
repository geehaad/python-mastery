'''Write a program called `pcost.py` that opens this file, reads
all lines, and calculates how much it cost to purchase all of the shares
in the portfolio. To do this, compute the sum of the second column
multiplied by the third column.'''
from Data import portfolio

def portfolio_cost(filename):
    total_cost = 0.0

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split(',')
                shares = int(parts[1])
                price = int(parts[2])
                total_cost += shares * price 

    except FileNotFoundError:
        print("Error: File '{filename}' not found")

if __name__ == 'main':
    filename = 'portfolio.csv'
    total_cost = portfolio_cost(filename)

    if total_cost is not None:
        print(f"Total cost of the portfolio: ${total_cost: .2f}")