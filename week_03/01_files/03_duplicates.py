'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

import hashlib
from os import listdir
from os.path import isfile, join

#provide a path and create a list of files

mypath = "/Users/Blake/Documents/learning/python-onsite/week_03/01_files"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

#hash all the files in the folder
hasher = hashlib.md5()
hashlist = []

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(2 ** 20), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


for i in onlyfiles:
    hashlist.append(md5(i))

print(hashlist)

#only uses unique values (files) in a new dictionary combines of two lists
my_dict = dict(zip(hashlist, onlyfiles))
print(my_dict)

#let the user know which files were not unique
for i in onlyfiles:
    if i not in my_dict.values():
        print(f"{i} is a duplicate")





