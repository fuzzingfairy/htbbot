
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
import django
django.setup()

from mysite.htb.models import  *

with open("data/data.json") as f:
    json = json.load(f)



for i in json:
    defaults = {
        "name":i["name"],
        "static_points":i["static_points"],
        "sp_flag": i["sp_flag"],
        "os":i["os"],
        "points":i["points"],
        "star":i["star"],
        "release":i["release"],
        "easy_month":i["easy_month"],
        "poweroff":i["poweroff"],
        "difficulty":i["difficulty"],
        "difficultyText":i["difficultyText"],
        "user_owns_count":i["user_owns_count"],
        "authUserInUserOwns":i["authUserInUserOwns"],
        "root_owns_count":i["root_owns_count"],
        "authUserInRootOwns":i["authUserInRootOwns"],
        "counterCake":i["feedbackForChart"]["counterCake"],                                                             
        "counterVeryEasy":i["feedbackForChart"]["counterVeryEasy"],                                                   
        "counterEasy":i["feedbackForChart"]["counterEasy"],                                                                  
        "counterTooEasy":i["feedbackForChart"]["counterTooEasy"],                                                     
        "counterMedium":i["feedbackForChart"]["counterMedium"],                                              
        "counterBitHard":i["feedbackForChart"]["counterBitHard"],                                                  
        "counterHard":i["feedbackForChart"]["counterHard"],                                                
        "counterTooHard":i["feedbackForChart"]["counterTooHard"],                                                   
        "counterExHard":i["feedbackForChart"]["counterExHard"],                                                 
        "counterBrainFuck": i["feedbackForChart"]["counterBrainFuck"],
}
    object = Box.objects.update_or_create(
        boxid = i["id"],
        defaults=defaults
        )

