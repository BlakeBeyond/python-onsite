'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''

lower = int(input("give me the lower range number: "))
upper = int(input("give me the upper range number: "))
for i in range(lower,upper):
    square = i * i
    print(square)