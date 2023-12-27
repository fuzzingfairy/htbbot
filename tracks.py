import tqdm
from utils.data import *
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *


print("Pick a track:")
tracks = Track.objects.all()
for idx,track in enumerate(tracks):
    all_boxes = Track.objects.get(name=track.name).boxes.all()
    to_do = Track.objects.get(name=track.name).boxes.filter(authUserInRootOwns=False)
    if len(to_do) == 0:
        print("Track: ",idx,track.name,"[Done]")
    else:
        print("Track: ",idx,track.name)

    

idx = int(input("Track number: "))
track = tracks[idx]


all_boxes = Track.objects.get(name=track.name).boxes.all()
to_do = Track.objects.get(name=track.name).boxes.filter(authUserInRootOwns=False)

for i in to_do:
    print(i.name, i.difficultyText)


picked = random.choice(to_do)
tqdm.tqdm(initial=len(all_boxes)-len(to_do),total=len(all_boxes),desc=picked.name,unit="boxes",unit_scale=False)
picked,now = load_start(picked)
print("Do: ",picked.name)
if input("Accept [Y/n]: ") not in ["Y","y"]:
    exit()

guide = input("Did you use  a guide [1/0]? ")
picked.authUserInRootOwns = True
finish = datetime.datetime.now()
elapsed = finish-now
picked.num_minutes = round(elapsed.seconds/60)
picked.save()