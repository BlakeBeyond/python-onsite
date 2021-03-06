'''
* BONUS TASK *
* DISCLAIMER: THIS IS PROBABLY HARD AND REQUIRES SOME TWEAKING *

Explore whether you can use the JavaScript support with requests_html,
to scrape the youtube comments from a video page you are interested in.
( you can use: https://www.youtube.com/watch?v=M54UFvJqQ5I )

Parse the content, locate the usernames of the people who commented,
and save all comments to file in the following form:

username:
    comment text

username:
    comment text

etc.

If requests_html doesn't quite make it and you want to learn more
about scraping dynamic page content, check out 'selenium'.

'''

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys
import urllib.request
import time

try: