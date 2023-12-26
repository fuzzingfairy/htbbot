import tqdm
from utils.data import *
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *



lines = open("data/tjnullstarter","r").read().split()

boxes = Box.objects.filter(authUserInRootOwns=False)


to_do = []

for i in boxes:
    if i.name in lines:
        to_do.append(i)

tqdm.tqdm(initial=len(lines)-len(to_do),total=len(lines),desc="Percentage TJnull starter Done",unit="boxes",unit_scale=False)

picked = random.choice(to_do)
picked,now = load_start(picked)
print("Do: ",picked.name)
guide = input("Did you use  a guide [1/0]?")

picked.authUserInRootOwns = True
picked.save()