'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
try:
    filename = integers.txt
    with open(filename) as f_object:
        number = f_object.readlines()
        first_number = number[0]
except IOError:
    msg = "not sure that will work for input and output"
    print(msg)
except ValueError:
    msg1 = "these values cannot be ran"
    print(msg1)
else:
    from math import pi
    print(first_number * pi)