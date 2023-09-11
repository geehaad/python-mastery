# Exercise 1.2 - Solution

# Solution code is shown in the exercise.

'''Write a program called `pcost.py` that opens this file, reads
all lines, and calculates how much it cost to purchase all of the shares
in the portfolio. To do this, compute the sum of the second column
multiplied by the third column.'''
import sys

def portfolio_cost(filename):
    total_cost = 0.0

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                shares = int(parts[1])
                price = float(parts[2])
                total_cost += shares * price 

    except FileNotFoundError:
        print("Error: File '{filename}' not found")

    return total_cost

if __name__ == '__main__':

    filename = 'Data/portfolio.dat'
    total_cost = portfolio_cost(filename)

    
    print(f"Total cost of the portfolio: {total_cost:.2f}")
   