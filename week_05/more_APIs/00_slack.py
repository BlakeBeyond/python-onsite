'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]

We will continue to work with this data throughout the week, so make sure to complete it!

at the end of url ther eis a specific identifierfor the channel
'''
from pprint import pprint
from slackclient import SlackClient
from json import dumps
from datetime import datetime

token = "xoxp-561901429298-572323878850-580987060964-4ebaee0b9a1ab391779a93b409488e37"
slack_args = {
    "python-resources": "CGUDWETHR",

}

sc = SlackClient("xoxp-561901429298-572323878850-580987060964-4ebaee0b9a1ab391779a93b409488e37")
chat_history = sc.api_call("channels.history",
            channel=slack_args['python-resources'])
#
# messages = chat_history["messages"]
# content = messages["text"]

messages = chat_history["messages"]
# pprint(messages)
list_ = []


try:

    for m in messages:
        links = {}
        # pprint(m)
        if 'https' in m["text"]:
            links["link"] = m["text"].strip("<>")
            try:
                links["description"] = m["attachments"][0]["text"]
            except KeyError:
                pass
            links["date_added"] = float(m["ts"])
            links["read"]=False
            links["rating"]=0
            try:
                links["comments"] = m["replies"]
            except KeyError as ke:
                # print(ke)
                links["comments"] = 0
            links["starred"] = False
            try:
                links["starred"] = m["is_starred"]
            except KeyError as er:
                # print(er)
                pass
            #print(links)
            list_.append(links)
            #pprint(list_)

except KeyError as e:

    print(e)
    pass
pprint(list_)

with open ("slack_data.json", "w") as write_file:
    json_string = dumps(list_)
    write_file.write(json_string)

'''

 {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
for m in messages:
    link = m['text'].strip('<>')
    pprint(link)

it requires a token
#use a method on that instance, the api call, that's just how the set it app
sc.api_call(
    "chat.postMessage",
    channel = slack_args
    text="text you want to post"
'''