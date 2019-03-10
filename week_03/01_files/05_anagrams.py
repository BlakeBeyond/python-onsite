
'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""
from anagram_sets import *
import all_anagrams, signature
import shelve


def store_anagrams(filename, anagram_map):
    shelf = shelve.open(filename, 'c')
    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    shelf = shelve.open(filename)
    sign = signature.word
    return shelf[sign]



