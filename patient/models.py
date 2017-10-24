# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from hospital_reg.models import hospital
from doctor.models import doctor
# Create your models here.
class patient(models.Model):
	p_name = models.CharField(max_length = 100)
	p_age = models.IntegerField()
	p_email = models.CharField(max_length = 100)
	p_phone_no = models.CharField(max_length = 100)
	p_address = models.CharField(max_length = 1000)
	p_gender = models.CharField(max_length = 1000)
	p_bloodgrp = models.CharField(max_length = 1000)
	p_dateofbirth = models.CharField(max_length=1000)
	user_id = models.ForeignKey(User)
	hospital_id = models.ForeignKey(hospital,on_delete = models.CASCADE)
	doctor_id = models.ManyToManyField(doctor)
	bill_amt = models.BigIntegerField(null=True, blank=True)
	profile_pic = models.ImageField(upload_to='patient_profile_pics/',null=True, blank=True)


	def __str__(self):
		return self.p_name

class appointment(models.Model):
	date_of_appointment = models.CharField(max_length = 100)
	from_time = models.CharField(max_length = 100)
	to_time = models.CharField(max_length = 100)
	cons_doctor = models.ForeignKey(doctor,on_delete = models.CASCADE)
	condition = models.CharField(max_length = 200)	
	note = models.CharField(max_length = 500,null=True, blank=True)
	book_patient = models.ForeignKey(patient,on_delete = models.CASCADE)
	confirm = models.BooleanField(default=False)
	hospital_id = models.ForeignKey(hospital,on_delete = models.CASCADE)