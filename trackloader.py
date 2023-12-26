
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *


lines = json.load(open("data/data.json","r"))
print(len(lines))
for track in lines:
    name =track["name"]
    des = track["description"]
    dif = track["difficulty"]
    defaults = {
        "description":des,
        "difficulty":dif,
        "staff_pick":track["staff_pick"]
    }

    boxestoadd = []
    for i in track["items"]:
        if i["type"] == "machine":
            box = Box.objects.filter(name=i["name"])[0]
            boxestoadd.append(box)
        
    if boxestoadd != []:
        track,_ = Track.objects.update_or_create(
        name = name,
        defaults=defaults
        )
        print(name)
        for i in boxestoadd:
            print(i.name)
            track.boxes.add(i)




exit()
track,_ = Track.objects.update_or_create(
    name = "TJNULL 2003 hard")



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



