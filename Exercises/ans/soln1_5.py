# Exercise 1.5 - Solution

# <!-- The solution is shown in the exercise description.


# [Back](ex1_5.md) -->

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    
s1 = Stock('gog', 10, 20)
print(s1.name)
