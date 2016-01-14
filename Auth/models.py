from django.db import models

# Create your models here.
class Authentication(models.Model):
	userid = models.CharField(max_length = 100) #primary key
	password = models.CharField(max_length = 100)

	def __str__(self):
		return self.userid

class Users(models.Model):
	userid = models.CharField(max_length = 100) #primary key
	name = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	contact = models.CharField(max_length = 12)
	profile_pic = models.CharField(max_length = 100)

	def __str__(self):
		return self.name