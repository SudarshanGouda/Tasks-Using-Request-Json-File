'''
create a list of websites
create a list of websites that DIDn't open properly (404)
save all these not opening websites into a file
save all  websites that are opening into another file
'''

import requests
with open('Yeswebsite.txt','w') as file:
    pass
with open('Nowebsite.txt','w') as file:
    pass

websites=['https://jsonplaceholder.typicode.com','https://docs.python.org/3/library','https://github.com',
          'https://www.youtube.com','http://www.google.com/blahblah']
for site in websites:
    try:
        r = requests.get(site)
        r.raise_for_status()
        with open ('Yeswebsite.txt','a') as file:
            file.write(site+'\n')
    except requests.exceptions.HTTPError as err:
        with open ('Nowebsite.txt','a') as file:
            file.write(site+'\n')
        raise SystemExit(err)