'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters (count)
- the total number of characters (len)

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

message = input("Type word: ")
message.replace(" ", "")

up = "Upper Case: " + str(sum(1 for c in message if c.isupper()))

low = "Lower Case: " + str(sum(1 for c in message if c.islower()))
punctuation = [".", "?", "!", ","]
punct = "Punctuation: "+ str(sum(1 for c in message if c in punctuation))
char = "Characters: " + str(len(message))
print(up)
print(low)
print(punct)
print(char)

dict_count = {"Upper Case": sum(1 for c in message if c.isupper()), "Lower Case": sum(1 for c in message if c.islower()), "Punctuation": sum(1 for c in message if c in punctuation), "Characters": len(message)}
print(dict_count)







