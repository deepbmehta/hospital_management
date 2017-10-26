# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from hospital_reg.models import hospital
from doctor.models import doctor
from patient.models import patient
from datetime import datetime
# Create your models here.

class labhead(models.Model):
	l_name = models.CharField(max_length=100)
	l_number = models.IntegerField()
	l_email = models.CharField(max_length=100)
	l_address = models.CharField(max_length=100)
	l_gender = models.CharField(max_length=100)
	l_age = models.IntegerField()
	l_salary = models.IntegerField()
	hospital_id = models.ForeignKey(hospital,on_delete = models.CASCADE)
	user_id = models.ForeignKey(User)
	def __str__(self):
		return self.l_name

class reports(models.Model):
	p_id = models.ForeignKey(patient,on_delete = models.CASCADE)
	r_title = models.CharField(max_length = 100)
	report = models.FileField(upload_to='reports/')
	created_date=models.DateTimeField(auto_now_add = True)
	details = models.TextField(blank=True, null=True)



		