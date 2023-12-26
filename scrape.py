import requests
import random
import time
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiNjE2YjZiZjcyMzMxMzY2YjEwMTI1YjQyNzcxZWVmNWFjMzcyNDU0Y2QzYWRjNjJjZjllYmUwOTBmZWVjN2Y4NTQ3MmIzYTA1OGRjYjM4MzMiLCJpYXQiOjE3MDM1MzY5NjkuNDUxNDI5LCJuYmYiOjE3MDM1MzY5NjkuNDUxNDMsImV4cCI6MTcwNjEyODk2OS40NDEyMTQsInN1YiI6Ijk1Mzc2NCIsInNjb3BlcyI6W119.LwDT-indLyTQnuhQ63hFbFoJPwIptIRkoEocXAXdVm3uft79GKQ3bylD1u-1bxPeW5Ro0iujNp6O_GPLXy-eSB-EcLZksqCvaL7NOsuDA2S52fnASt3BcX4v3UNcAZNBtKRc7tBwl8MMPm68v7DORgrHhVPjPBu3X1uGxfJQbinQZoHZzw37GTY3DDClkG67iTUUocckwYIIsv6clRwO0ruJElYMKdKNYQMTDGRS4WsEnewwMH6tV4V5K6Jf1TIefl4huHWU87Aw31Z-WfK6EYBml4-Jofh_mmUbRm5fF3hbc_ySZFvnXg5On3BcZ32kT0cpCjjVVGaR0vhIcRNkP5PzCdoJW_Un9_EoCoVZf9Ew4Q3V3hLmz_cQ3XSMO2a5ajqOBbQuArrX8RRFoYbSQloVVaDjljIJ-ovxJ2CpwHN4NDv_g4xyBk6RnknQvP73v2XAklXoY26f_tpIax_2NLF8oVrelrZG8s_zeUNLaTWQKFidAF58n66oNz3Km5KzE1BsbJJnUQKM-1lefvobVHlR1FbOmvEmo59qHbEbaLsD67QMN1D23HHtG89ndhcca5cLv0FlC_queDaR-DeiQvt0leheFwHneZTLDY0hyvl9GZgE0D4Mh6gw40u2s6l9vsyHqjuRgIM-fokEmNtHxGx3s8dvkQa4TjvdUJ7pcSU"

headers = {
    "Authorization":"Bearer " + jwt,
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

def scrapeBoxes():
    results = []
    for i in range(24):
        time.sleep(random.randrange(3,9))
        req = requests.get("https://labs.hackthebox.com/api/v4/machine/list/retired/paginated?sort_type=desc&page=" +str(i+1),proxies=proxies,headers=headers,verify=False)
        results.append(json.loads(req.text)['data'])


    with open('data/data.json','w') as f:
        json.dump(results, f)

res = []
def scrapeTracks():
    req = requests.get("https://labs.hackthebox.com/api/v4/tracks",proxies=proxies,headers=headers,verify=False)
    for i in json.loads(req.text):
        print(i["id"])
        time.sleep(random.randrange(4,9))
        req = requests.get("https://labs.hackthebox.com/api/v4/tracks/"+str(i["id"]),proxies=proxies,headers=headers,verify=False)
        res.append(json.loads(req.text))

    with open('data/data.json','w') as f:
        json.dump(res, f)



if __name__ == "__main__":
    scrapeTracks()