'''
Write a script that connects to the http://numbersapi.com/ and fetches trivia on all
numbers from 0 through 100.

Store the responses in a new JSON file called numbers.json

BONUS:
* fetch information of all the prime numbers from 1-1000
* cycle through the different endpoints the API provides (trivia, math, date, year)
  in a way that they change in binary chunks, e.g.:
  - the info on the first 2 numbers are of type trivia
  - info on the next 4 numbers are of type math
  - the next 8 are on dates
  - etc. (cycle back to the trivia after year)

'''
import requests
from pprint import pprint
from json import dumps
resp_dict = {}
for num in range(0, 101):
    url = f"http://numbersapi.com/{num}?type=trivia&notfound=floor&fragment"
    # if num == 7 or num == 36:
    #     pass
    # else:
    r = requests.get(url)
    resp_dict[num] = r.text
pprint(resp_dict)

# with open ("numbers.json", "w") as write_file:
#     json_string = dumps(resp_dict)
#     write_file.write(json_string)
