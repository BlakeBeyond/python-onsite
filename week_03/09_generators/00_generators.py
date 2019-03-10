'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(firstn(100))

for i in firstn(100):
    print(i)