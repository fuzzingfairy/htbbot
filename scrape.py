import requests
import random
import time
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "Authorization":"Bearer " + input("jwt token: "),
    "Accept":"application/json, text/plain, */*",
    "Origin":"https://app.hackthebox.com",
    "Referer":"https://app.hackthebox.com/",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua":"",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Sec-Ch-Ua-Platform":"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36"

}

proxies = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

results = []
for i in range(24):
    time.sleep(random.randrange(3,9))
    req = requests.get("https://labs.hackthebox.com/api/v4/machine/list/retired/paginated?sort_type=desc&page=" +str(i+1),proxies=proxies,headers=headers,verify=False)
    results.append(json.loads(req.text)['data'])


with open('data/data.json','w') as f:
    json.dump(results, f)
