'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.

'''
my_dict = {}
sorted_list = []

def most_frequent(fstring_):

    for ch in fstring_:
       if ch not in my_dict:
           my_dict[ch] = fstring_.count(ch)

    for key, value in sorted(my_dict.items(), key=lambda v: v):
        sorted_list.append(key)
    print(sorted_list)


function_output = most_frequent("kanapka")




