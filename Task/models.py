from __future__ import unicode_literals

from django.db import models
from decimal import Decimal

from django.utils import timezone
# Create your models here.
class Tasks(models.Model):
	#taskid = models.CharField(max_length = 100, primary_key=True) #primary key
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	start_date = models.DateTimeField(default = timezone.now,blank = True)
	due_date = models.DateTimeField(default = timezone.now,blank = True)
	repeat = models.BooleanField(default = 0)
	set_reminder_before = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	
	
	def __str__(self):
		return self.title