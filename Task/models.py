from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
# Create your models here.
class Tasks(models.Model):
	taskid = models.CharField(max_length = 100, primary_key=True) #primary key
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	creation_date = models.DateTimeField(default = timezone.now,blank = True)
	due_date = models.DateTimeField(default = timezone.now,blank = True)
	is_rotation = models.BooleanField(default = 0)
	remind_before = models.DateTimeField(default = timezone.now,blank = True)
	
	
	def __str__(self):
		return self.title
