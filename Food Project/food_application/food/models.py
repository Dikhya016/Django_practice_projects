from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=200,blank=True)
    description=models.CharField(max_length=300,blank=True)
    address=models.CharField(max_length=300,blank=True)
    price=models.IntegerField(null=False)
    rating=models.DecimalField(max_digits=5, decimal_places=1,blank=True)
    image=models.CharField(max_length=500,default='https://cdn-icons-png.flaticon.com/256/1516/1516233.png',blank=True)
    def __str__(self):
        return self.name