'''
Create an account at freecycle or use the following:
user: martin-martin
pwd:  bali2019

Using python's request_html library:
* log in to the website
* navigate to the site that contains all posts for the Denver, CO group
* retrieve all post titles from the first page
* save the titles to a file called 'denver_posts.txt'

BONUS: use pagination features to retrieve all posts of all pages in the group
       and save them to the file

'''

import requests_html
from requests_html import HTMLSession
payload = {'username': 'martin-martin', 'pass': 'bali2019'}
url = 'https://my.freecycle.org/login'
session = HTMLSession()
r = session.post(url, data=payload)
for link in r.html.absolute_links:
    if link.endswith("DenverCO"):
        url = link
print(url)
r = session.get(url)
c1_titles = r.html.find(".candy1")
c2_titles = r.html.find(".candy2")
#we're using dot cause we lookin' for dem class namez
all_titles = c1_titles + c2_titles


with open ("denver_posts.txt", "w") as file_object:
    for i in all_titles:
        file_object.write(i.text)



