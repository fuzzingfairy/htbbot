import csv
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *


with open('data/times.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row['name'],row['num_minutes'])
        box = Box.objects.filter(name=row['name'])[0]
        box.num_minutes = row['num_minutes']
        box.save()