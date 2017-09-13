# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class hospital(models.Model):
	hos_name = models.CharField(max_length = 500)
	hos_num1 = models.BigIntegerField()
	hos_num2 = models.BigIntegerField(null = True,blank = True)
	hos_email = models.CharField(max_length = 100)
	hos_street = models.CharField(max_length = 500)
	hos_location = models.CharField(max_length = 100)
	hos_city = models.CharField(max_length = 100)
	hos_state = models.CharField(max_length = 100)
	hos_landmark = models.CharField(max_length = 100,null = True,blank = True)
	hos_pincode = models.CharField(max_length = 100)
	hos_registration_no = models.CharField(max_length = 100,unique = True)
	hos_weblink = models.CharField(max_length = 100,null=True,blank = True)
	user_id = models.ForeignKey(User)
	

	def __str__(self):
		return self.hos_name
	
# Create your models here.





class user_type(models.Model):
    types = models.IntegerField()
    user_detail = models.ForeignKey(User)
    

    def __str__(self):
        return str(self.types)