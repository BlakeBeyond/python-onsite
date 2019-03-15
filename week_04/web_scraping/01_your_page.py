'''
Using python's request library, retrieve the HTML of the website you created
that now lives online at <your-gh-username>.github.io/<your-repo-name>

BONUS: extend your python program so that it reads your original HTML file
       and returns True if the HTML from the response is the same as the
       the contents of the original HTML file.

'''

import requests

url = "https://blakebeyond.github.io/blakebeyond/"
direct = 'file://localhost/Users/Blake/PycharmProjects/week2/gh-pages/index.html'
res = requests.get(url)


print(res.content)
if res.content == direct:
    print(True)
else:
    print(False)


