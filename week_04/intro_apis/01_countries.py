'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

import requests

url_home = 'https://restcountries.eu/rest/v2/name/poland?fullText=true'
url_current = 'https://restcountries.eu/rest/v2/name/indonesia?fullText=true'
h = requests.get(url_home)
c = requests.get(url_current)
hj = h.json()
cj = c.json()

pol_pop = hj[0]['population']
ind_pop = cj[0]['population']
if pol_pop > ind_pop:
    print(f"Polish population of {pol_pop} is bigger")
else:
    print(f"Indonesiain population of {ind_pop} is bigger")
difference = ind_pop - pol_pop
print(f"The difference is {difference}")

pol_cap = hj[0]['capital']
ind_cap = cj[0]["capital"]
pol_native = hj[0]['nativeName']
ind_native = cj[0]["nativeName"]

print(pol_cap)
print(ind_cap)
print(pol_native)
print(ind_native)

