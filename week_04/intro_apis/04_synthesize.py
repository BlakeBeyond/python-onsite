'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and present it to class ;)

'''
import requests
from pprint import pprint
import json
URLcn = 'https://api.chucknorris.io/jokes/random'

cnr = requests.get(URLcn)

funny_dict = {}
data = (cnr.json())
joke = data['value']
word_list = joke.split()
old_joke = word_list[-1]
new_joke = old_joke.replace(".", "")
print(new_joke)


URLdm = f'https://api.datamuse.com/words?rel_rhy={new_joke}'
dmr = requests.get(URLdm)
rhymes = (dmr.json())
funny_list = []
for i in rhymes:
    funny_list.append(i["word"])
    funny_dict[joke] = funny_list
print(funny_dict)

#no time to rhyme, crypto APIs await

