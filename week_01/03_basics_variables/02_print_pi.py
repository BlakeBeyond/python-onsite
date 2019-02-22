'''
Print pi to the console using the following formula:
note that this is not the complete series to compute the true number pi.
Challenge: find another way to do this using a package you can import

4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))

'''

x = 4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))

#I'm importing pi from math package
import math
# the command for the challenge is print(math.pi)
#I find out what's missing from the x
y = x / math.pi
#I transform the equation so it's = pi and print
print(x / y)