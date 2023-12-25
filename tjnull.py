import tqdm
from utils.data import *
import random

_, not_done = load_boxes()


lines = open("data/tjnullstarter","r").read().split()


to_do = []
for i in lines:
    for j in not_done:
        if i == j["name"]:
            to_do.append(j)

tqdm.tqdm(initial=len(lines)-len(to_do),total=len(lines),desc="Percentage TJnull Done",unit="boxes",unit_scale=False)

picked = random.choice(to_do)
picked,now = load_start(picked)
print("Do: ",picked['name'])
guide = input("Did you use  a guide [1/0]?")

write_done([picked['name']])
write_times(now,guide,picked)