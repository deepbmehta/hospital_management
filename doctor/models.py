# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from hospital_reg.models import hospital
from django.db import models

# Create your models here.
class doctor(models.Model):
	d_name = models.CharField(max_length = 1000)
	d_email = models.CharField(max_length = 1000)
	d_phone_no = models.BigIntegerField()
	d_address = models.CharField(max_length = 1000)
	d_spec = models.CharField(max_length = 1000)
	d_work_exp = models.IntegerField()
	d_degree = models.CharField(max_length = 1000)
	d_salary = models.IntegerField()
	d_gender = models.CharField(max_length = 10)
	user_id = models.ForeignKey(User)
	d_hospital_id = models.ForeignKey(hospital, on_delete = models.CASCADE)

	def __str__(self):
		return self.d_name




	#image-profilepic