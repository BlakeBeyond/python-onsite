'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

word_list = []
with open('words.txt') as file_object:
    contents = file_object.read().split()
    for i in contents:
        if len(i) >= 20:
            word_list.append(i)
print(word_list)

