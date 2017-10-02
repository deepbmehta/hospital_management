# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from hospital_reg.models import hospital
from doctor.models import doctor
from patient.models import patient
# Create your models here.

class cashier(models.Model):
	c_name = models.CharField(max_length=100)
	c_number = models.IntegerField()
	c_email = models.CharField(max_length=100)
	c_address = models.CharField(max_length=100)
	c_gender = models.CharField(max_length=100)
	c_age = models.IntegerField()
	c_salary = models.IntegerField()
	hospital_id = models.ForeignKey(hospital,on_delete = models.CASCADE)
	user_id = models.ForeignKey(User)
	def __str__(self):
		return self.c_name


class invoice(models.Model):
	p_id = models.ForeignKey(patient,on_delete = models.CASCADE)
	i_amount = models.IntegerField()
	bills = models.FileField(upload_to='invoices/')


