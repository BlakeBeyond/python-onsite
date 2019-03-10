'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
def my_enumerate(iterable_object):
    for i in range(len(iterable_object)):
    print(f"{i}: {iterable_object[i]} python")
