'''
JsonPlaceholder

JSONPlaceholder comes with a set of 6 common resources:

/posts	100 posts
/comments	500 comments
/albums	100 albums
/photos	5000 photos
/todos	200 todos
/users	10 users

'''

import requests
import json

responce= requests.get('https://jsonplaceholder.typicode.com/todos')

print(responce.text)

todo=json.loads(responce.text)

print(todo)

print(todo[4])