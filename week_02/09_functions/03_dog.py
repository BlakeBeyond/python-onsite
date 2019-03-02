'''
Write a program with the following three functions:

    - bark - this method should not take in any arguments and should print the string "bark bark"
    - eat - takes in parameters food_item and amount and prints out "The dog ate <amount> of <food_item>
    - sleep - calls the python sleep method to sleep the program for 5 seconds.



'''

import time


def sleep():
    time.sleep(5)


flag = True
while flag:
    for i in range(1, 11):
        print("bark bark")
        i += i
        if i == 10:
            flag = False


def eat(food_item, amount):
    print("Dog ate", amount, "of", food_item)


