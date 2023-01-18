import requests as r
import json
import pandas as pd

responce=r.get('https://jsonplaceholder.typicode.com/todos')

files=json.loads(responce.text)

with open('Sample.json','w',encoding='UTF-8') as f:
    json.dump(files,f,ensure_ascii=False)

df=pd.read_json('Sample.json')

print(df.head())