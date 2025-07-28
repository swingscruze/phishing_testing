from django.db import models

# Create your models here.



class user(models):
    username = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()





    
