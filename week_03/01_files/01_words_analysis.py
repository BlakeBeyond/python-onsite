'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
min_words = []
max_words = []
word_dict = {}
with open('words.txt') as file_object:
    contents = file_object.read().split()
    print(contents)
    for i in contents:
        word_dict[i] = len(i)
    print(word_dict)
    for k, v in word_dict.items():
        if v == min(word_dict.values()):
            min_words.append(k)
        if v == max(word_dict.values()):
            max_words.append(k)
    print(min_words)
    print(max_words)
    print(len(contents))




