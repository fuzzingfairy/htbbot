import random
import json
import csv
import tqdm

with open("data.json","r") as f:
    data = json.load(f)

real = []
for i in data:
    real += i

count = 0
total = len(data)
for i in real:
    if i['authUserInRootOwns']:
       # print(count)
        count += 1


tqdm.tqdm(initial=count,total=len(real),desc="Percentage HTB Owned",unit="boxes",unit_scale=False)