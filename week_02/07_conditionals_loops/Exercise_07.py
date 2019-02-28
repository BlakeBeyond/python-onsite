'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''
num = 1001
while num >= 1:
    num -= 3
    if num > 0:
        print(num)