from django.db import models

class Box(models.Model):
    boxid = models.IntegerField()
    name = models.CharField(max_length=30)
    static_points = models.IntegerField()
    sp_flag = models.IntegerField()
    os = models.CharField(max_length=30)
    points = models.IntegerField()
    star = models.FloatField()
    release = models.CharField(max_length=30)
    easy_month = models.IntegerField()
    poweroff = models.IntegerField()
    difficulty = models.IntegerField()
    difficultyText = models.CharField(max_length=30)
    user_owns_count = models.IntegerField()
    authUserInUserOwns = models.BooleanField()
    root_owns_count = models.IntegerField()
    authUserInRootOwns = models.BooleanField()
    counterCake = models.IntegerField()                                                                  
    counterVeryEasy = models.IntegerField()                                                             
    counterEasy = models.IntegerField()                                                                   
    counterTooEasy = models.IntegerField()                                                                
    counterMedium = models.IntegerField()                                                                
    counterBitHard = models.IntegerField()                                                                 
    counterHard = models.IntegerField()                                                                    
    counterTooHard = models.IntegerField()                                                              
    counterExHard = models.IntegerField()                                                                   
    counterBrainFuck = models.IntegerField()  
    predicted_minutes = models.IntegerField(default=None, blank=True,null=True)  
    num_minutes = models.IntegerField(default=None, blank=True,null=True)  



class Track(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    difficulty = models.CharField(max_length=30)
    staff_pick = models.IntegerField()
    boxes = models.ManyToManyField(Box)
