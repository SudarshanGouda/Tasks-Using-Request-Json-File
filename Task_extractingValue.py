import requests
import json

responce = requests.get('https://jsonplaceholder.typicode.com/todos')

try:
    task = json.loads(responce.text)
except json.decoder.JSONDecodeError:
    print('Its not a json file')
else:  # If try works properly it comes to else
    results=dict()
    for entry in task:
        if entry['completed'] == True:
            try:
                results[entry['userId']]+=1
            except KeyError:
                results[entry['userId']] = 1
print(results)
print(results.items())
print(results.values())
print(max(results.values()))

for userid, CompletedTask in results.items():
    # print(userid, CompletedTask)
    if CompletedTask==max(results.values()):
        print(f'User id with maximum Task completed :{userid}')