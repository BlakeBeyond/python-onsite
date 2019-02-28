'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''



list_ = (input('Enter numbers with spaces : ')).split()

f_list = []

for item in list_:
    f_list.append(float(item))

f_list.sort()

if len(f_list) % 2 != 0:
    f_list.append(float(0))

#create pairs
#print('Length ',len(f_list))

tuple_pair_list = []

for i in range(0, len(f_list), 2):
    tuple_pair = (f_list[i], f_list[i+1])
    tuple_pair_list.append(tuple_pair)

print('Tuple Pair List', tuple_pair_list)


for pair in tuple_pair_list:
    print(pair)