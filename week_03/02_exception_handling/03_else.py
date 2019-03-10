'''
Write a script that demonstrates a try/except/else.

'''
filename = "virus.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file" + filename + "does not exist, or is saved in a different location"
else:
    print(contents)