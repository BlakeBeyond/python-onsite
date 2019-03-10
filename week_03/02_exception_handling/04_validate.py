'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
try:
    number1 = input("Give an integer pls: ")
except TypeError:
    msg = "You sure that was an integer? I think not..., try again and be nice this time"
    print(msg)
    number1 = input("Give an integer pls: ")
else:
    print("you won" + number1 + "eggs")