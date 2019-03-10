'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    number1 = input("give me a number: ")
    number2 = input("and a number to divide it by: ")
    quotient = int(number1) / int(number2)
    print(quotient)
except TypeError:
    msg = "Told you to give me a number, not a word"
    print(msg)
except ZeroDivisionError:
    msg0 = "Can't divide by 0, you crazy?"