
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *


lines = open("data/tjnullhard","r").read().split()

track,_ = Track.objects.update_or_create(
    name = "TJNULL 2003 hard")


for i in lines:
    print(i)
boxes = Box.objects.all()
print()
print()
added = 0
for i in boxes:
    if i.name in lines:
        print(i.name)
        track.boxes.add(i)
        added +=1 
print(added)



