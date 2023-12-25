import tqdm
from utils.data import *
import random

_, not_done = load_boxes()


lines = open("data/tjnullstarter","r").read().split()


to_do = []
for i in lines:
    for j in not_done:
        if i == j["name"]:
            to_do.append(i)

tqdm.tqdm(initial=len(lines)-len(to_do),total=len(lines),desc="Percentage TJnull",unit="boxes",unit_scale=False)

picked = random.choices(to_do,k=3)
while len(set(picked)) != 3:
    picked = random.choices(to_do,k=3)

for i in picked:
    print("Do: ",i)