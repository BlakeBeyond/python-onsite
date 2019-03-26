'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import tweepy
import bl
import json
from pprint import pprint

auth = tweepy.OAuthHandler(bl.consumer_key, bl.consumer_secret)
auth.set_access_token(bl.access_token, bl.access_token_secret)
api = tweepy.API(auth)
user = '@jordanbpeterson'
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    pprint(friend)


f = api.followers_ids("@jordanbpeterson")
print(f)
# dic = {}
# try:
#     for i in f:
#         followers = api.followers_ids(i)
#         friends = api.friends_ids(i)
#         dic[i] = [len(followers), len(friends)]
# except Exception as err:
#     print(err) # [{'message': 'Rate limit exceeded', 'code': 88}]
# print(dic)


