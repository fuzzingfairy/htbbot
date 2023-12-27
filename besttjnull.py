import tqdm
from utils.data import *
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *

tracks = Track.objects.all().order_by('name')
boxes = {}

todoset = set()
allboxset = set()

for idx,track in enumerate(tracks):
    if "TJNULL" in track.name:
        to_do = Track.objects.get(name=track.name).boxes.filter(authUserInRootOwns=False)
        for i in to_do:
            if i.name in boxes:
                boxes[i.name] = [boxes[i.name][0]+1,boxes[i.name][1]]
            else:
                boxes[i.name] = [0,i]
        
        allboxes = Track.objects.get(name=track.name).boxes.all()
        for i in allboxes:
            allboxset.add(i.name)



boxes = {k: v for k, v in sorted(boxes.items(), key=lambda item: item[1][0])}
for i in reversed(boxes):
    picked = boxes[i][1]
    rank = boxes[i][0]
    break


tqdm.tqdm(initial=len(allboxset)-len(boxes),total=len(allboxset),desc=picked.name,unit="boxes",unit_scale=False)
picked,now = load_start(picked)
print("Do: ",picked.name,"rank",rank)
if input("Accept [Y/n]: ") not in ["Y","y"]:
    exit()

guide = input("Did you use  a guide [1/0]? ")
picked.authUserInRootOwns = True
finish = datetime.datetime.now()
elapsed = finish-now
num_minutes = round(elapsed.seconds/60)
print("Done in",num_minutes)
picked.num_minutes = num_minutes
picked.save()

        