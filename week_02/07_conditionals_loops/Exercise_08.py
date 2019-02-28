'''
Demonstrate the use of the "break" statement to exit a loop.

'''
name = input("do you want to break the loop?: ")
while name != 'yes':
    name = input("do you want to break the loop?: ")
    if name == "no":
        continue

    if name == "yes":
        break
print("First day outta feds")