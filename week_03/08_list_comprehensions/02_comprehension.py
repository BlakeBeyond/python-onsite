'''
Using list comprehension, create a list that contains the individual
letters using the word "CodingNomads".

For example:

word = "CodingNomads"
..your code
result_list = ['C', 'o', 'd', 'i', 'n', 'g', 'N', 'o', 'm', 'a', 'd', 's']

'''
word = "CodingNomads"
result_list = [ch for ch in list(word)]
print(result_list)