'''
Using requests_html scrape information from a wikipedia page that interests you.
( you can use: https://en.wikipedia.org/wiki/Ubud )

Collect:
* all the information recorded in the infobox on the right
* 2 links to images on the site
* an interesting fact or quote from the page
* a collection of all the resources (titles and links) related to the page

Store the information in a nicely formatted text file.

'''

from requests_html import HTMLSession

url = "https://en.wikipedia.org/wiki/Zoroastrianism"
session = HTMLSession()
r = session.get(url)

box = r.html.xpath('//*[@id="mw-content-text"]/div/table[1]', first=True)
print(box.text)


box1 = r.html.find('#mw-content-text > div > table.vertical-navbox.nowraplinks', first=True)
print(box1.text)
#div is a child element, vertcial navbox issa class

two_img = r.html.find('img')
print(two_img[0])
print(two_img[1])


ref_collection = r.html.find('p', containing='purpose in life', first=True)
print(ref_collection.text)

all_links = r.html.absolute_links
print(all_links)

all_titles = r.html.find('title')
for i in all_titles:
    print(i.text)

i1 = two_img[0].attrs["src"]
i2 = two_img[1].attrs["src"]
t = all_titles[0].text
with open("02_wikipedia.txt", 'a') as file_object:
    file_object.write(f"{box.text}\n")
    file_object.write(f"{box1.text}\n")
    file_object.write(f"{i1}\n)")
    file_object.write(f"{i2}\n")
    file_object.write(f"{t}\n")
    for i in all_links:
        file_object.write(f"{i}\n")


