
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *


lines = open("data/tjnulloriginal","r").read().split()

#lines = ["Gobox"]
print(len(lines))
for _ in [1]:
    name = "Ismael Rodriguez OSCP top 10"
    des = ""
    dif = "Medium"
    defaults = {
        "description":des,
        "difficulty":dif,
        "staff_pick":0
    }

    boxestoadd = []
    """
    for i in track["items"]:
        if i["type"] == "machine":
            box = Box.objects.filter(name=i["name"])[0]
            boxestoadd.append(box)
    """

    for i in lines:
        print(i)
        box = Box.objects.filter(name__icontains=i)[0]
        boxestoadd.append(box)
    print(boxestoadd)
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



