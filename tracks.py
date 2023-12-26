import tqdm
from utils.data import *
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *


print("Pick a track:")
tracks = Track.objects.all()
for idx,i in enumerate(tracks):
    print("Track: ",idx,i.name)

idx = int(input("Track number: "))
track = tracks[idx]


all_boxes = Track.objects.get(name=track.name).boxes.all()
to_do = Track.objects.get(name=track.name).boxes.filter(authUserInRootOwns=False)


tqdm.tqdm(initial=len(all_boxes)-len(to_do),total=len(all_boxes),desc="Percentage TJnull starter Done",unit="boxes",unit_scale=False)

picked = random.choice(to_do)
picked,now = load_start(picked)
print("Do: ",picked.name)
guide = input("Did you use  a guide [1/0]?")

picked.authUserInRootOwns = True
picked.save()