'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

print([x.startswith('D') for x in names])


listcomp = lambda x: [i.startswith('D') for i in x]
print(listcomp(names))