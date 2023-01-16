import requests
import json

websites=['https://jsonplaceholder.typicode.com/todos','https://jsonplaceholder.typicode.com/posts','https://github.com']

for site in websites:
    ext_site=requests.get(site)
    try:
        print(json.loads(ext_site.text))
    except json.decoder.JSONDecodeError:
        print('Its not a json file')
