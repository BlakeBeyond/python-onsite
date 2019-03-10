'''
Write a script with a function that demonstrates the use of **kwargs.

'''

value_list = []


def you_write_a_script(**kwargs):
    if kwargs is not None:
        for value in kwargs.values():
            value_list.append(value)