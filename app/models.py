from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	id = models.CharField(primary_key=True,max_length=100)
	real_name = models.CharField(max_length=100,null=True,blank=True)
	tz = models.CharField(max_length=100,blank=True,null=True)
	

class ActivityPeriods(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	start_time = models.CharField(max_length=100,null=True,blank=True)
	end_time = models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return self.user.real_name