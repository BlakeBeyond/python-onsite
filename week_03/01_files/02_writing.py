'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

word_list = []
with open('words.txt') as file_object:
    contents = file_object.read().split()
    contents.reverse()
    print(contents)
filename = 'words_reverse.txt'
with open(filename, 'w') as file_object:
    for i in contents:
        file_object.write(i)




