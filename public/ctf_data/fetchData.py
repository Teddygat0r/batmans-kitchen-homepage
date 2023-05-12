# simple script that scrapes ctftime for most recent ctf data, then formats it into the ctf_data.json file properly.

from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

ctfs = requests.get('https://ctftime.org/team/3135', headers=headers)
soup = bs(ctfs.text,'html.parser')

iter = soup.table

data = {"ctfs": []}

#Gets data from the CTFTime API. Repeats itself cuz the api likes to shit itself every once in a while.
def fetchDataRepeat(link):
    ctfs = requests.get(f'https://ctftime.org/api/v1/{ link }', headers=headers)
    if "Forbidden" in ctfs.text:
        return fetchDataRepeat(link)
    return json.loads(ctfs.text)


for i in range(5):
    ctf = iter.contents[2 * i + 3]
    content = fetchDataRepeat(f'events/{ ctf.contents[2].contents[0]["href"][7:] }/')
    dt = {
        "date": content["finish"],
        "logo": content["logo"],
        "desc": content["url"]
    }
    data["ctfs"].append({
        "ctf": ctf.contents[2].getText(),
        "placement": ctf.contents[1].getText(),
        "data": dt
    })

    #limit 5 ctfs, if there are less than 5 break.
    if(2 * i + 5 > len(iter)): break

with open("ctf_data.json", "w") as outfile:
    outfile.write(json.dumps(data, indent=4))