import requests
import random
import time
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiOTEwZTEzMTBkNjI1ZGZkYjRhM2RlOWZhN2I1N2NkZmY2YmVmYzg3MGRhMzdkMzc3M2QzN2QxNzQ5NTdkZDY0MmM2MjNlYTEwZGVlMDc4OWMiLCJpYXQiOjE3MDMyODIxMzYuOTQ5NzE0LCJuYmYiOjE3MDMyODIxMzYuOTQ5NzE2LCJleHAiOjE3MDMyODU3MzYuOTMxNTc0LCJzdWIiOiI5NTM3NjQiLCJzY29wZXMiOltdfQ.OYILmkO2flZ6mL7bQMYW6RX7YjRQt7A-fKlfP-ulWHpLhHaB5DADIhXl5g1sl9Rnm3r3r9FZ7A80gVd3gpwf3BdgBon7e62o4wM5TVx8lT4uL-uFBzdzEvLxnt-Ij0E56AdN7xGOXWR5mtIwnxu1b8J_iXXzvZTOmwpgyUslOKPAYxLccqYblA692NBsCLJgBgi-RW5z4R_9fwcgmYGkYzUhDFzc1Iqggj4R89QdJEo_YBUbyHk83FzColamQ7YmH6dxYPaQ8uWKgFWecp4WIQUGSsM-nGlEAbKiB27BQ5wa6p400BbJ2gsA24Vul0NK3pKy25jXUDOai36J7yhOSjfkssNtpCrEeWZg8wNuNKVjWjT8YXyOYdo7IQZYVb-R1tS3I_2vAqZCLQkHoKN9Bhgk97c9zb5QcJW-ZDKxnbZNT7WVWszNHaurq6MBYpeBMO82sg0RlFgrUieb5cZILz6kma3fMbSj1rowM7rojx1vyyFaQsZTQ1zkQLwg_gsMOS52aLUvdQohsH4RDF738Glj6nVe_Ra3agVtjmM_-QJTsUev4XAarv0I0caxGNitXGHArQNzLB2Xadb74qH4MEeoucHkXM0vmMbz2rL1kbdcSzp58qbjP7pzStOM_HZNL1dh3XaacQnHf-YdRGUynmyfdxlFJOmGvjxPKUNtX5E",
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


with open('data.json','w') as f:
    json.dump(results, f)

import pdb;pdb.set_trace()