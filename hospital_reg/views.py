# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospital_reg.models import *
from doctor.models import *
from patient.models import *
from labhead.models import *
from cashier.models import *
from django.contrib.auth import authenticate,login,logout
import smtplib
import re
import hashlib
from email.MIMEMultipart import MIMEMultipart
from hospital_reg.safe import usermail,upassword
from email.MIMEText import MIMEText
#from patient.views import patientHome
import datetime



# Create your views here.
def homepage(request):
	return render(request, 'index.html')


def login_site(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = username, password = password)

		if user:
			login(request, user)
			if user_type.objects.get(user_detail = request.user).types == 1:
				return redirect('/hospitalHome/')
			if user_type.objects.get(user_detail = request.user).types == 2:
				return redirect("/docHome/")
			if user_type.objects.get(user_detail = request.user).types == 3:
				return redirect('/patientHome/')
			if user_type.objects.get(user_detail = request.user).types == 4:
				return redirect('/labHome/')
			if user_type.objects.get(user_detail = request.user).types == 5:
				return redirect('/cashierHome/')
								
		else:
			context = {}
			context['error'] = "Wrong username or password"
			return render(request, 'login.html',context)	


	else:
		context = {}
		context['error'] = ''	
		return render(request, 'login.html',context)



def logout_site(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('/login/')
	else:
		return HttpResponse('You need to log in')

def hos_reg(request):
	if request.method == 'POST':

		name = request.POST['name']
		license = request.POST['lic_no']
		email = request.POST['email']
		phone1 = request.POST['phone1']
		phone2 = request.POST['phone2']
		street = request.POST['street']
		location = request.POST['location']
		landmark = request.POST['landmark']
		city = request.POST['city']
		state = request.POST['state']
		pin_code = request.POST['pin_code']
		weblink =  request.POST['website']

		hash = hashlib.sha1()
		now = datetime.datetime.now()
		hash.update(str(now)+email+'game_of_thrones')
		tp=hash.hexdigest()



		user=User.objects.create(username=email,password=tp)
		user.save()

		hos = hospital.objects.create(hos_name = name,hos_num1 = phone1,hos_num2 = phone2,hos_email = email,hos_street = street,hos_location = location,hos_city = city,hos_state = state,hos_landmark = landmark,hos_pincode = pin_code,hos_registration_no = license,hos_weblink = weblink,user_id = user)
		hos.save()

		utype = user_type.objects.create(user_detail=user,types=1)
		utype.save()
      


		fromaddr=usermail
		toaddr=email
		msg=MIMEMultipart()
		msg['From']=fromaddr
		msg['To']=toaddr
		msg['Subject']='Confirmational Email'
		domain = request.get_host()
		scheme = request.is_secure() and "https" or "http"
		body = "Please Click On The Link To complete registration: {0}://{1}/{2}/changepass".format(scheme,domain,tp) 
		part1 = MIMEText(body, 'plain')
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, upassword)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()

		return HttpResponse('Check your mail box to confirm')
	else:
		return render(request,'hos_form.html')




def hos_reg_complete(request,p):
	if request.method=='POST':
		print p
		upass=request.POST.get('upass')
		upass1=request.POST.get('upass1')
		if upass==upass1:
			up=User.objects.get(password=p)
			print up
			up.set_password(upass)
			print up.password
			up.save()
			return redirect('/login/')
		else:
			return HttpResponse('Enter password correctly')
	else:
		up=User.objects.get(password=p)
		print up
		return render(request,'changepass.html',{ 'user':up })
				

    #     print p
    #     upass=request.POST.get('upass')
    #     upass1=request.POST.get('upass1')
        

    #     if upass==upass1:
    #         up=User.objects.get(password=p)
    #         print up


    #         up.set_password(upass)
    #         print up.password
    #         up.save()

            

    #         return redirect('/login/')

    #     else:
    #         return HttpResponse('Enter password correctly')

    # else:
    #     up=User.objects.get(password=p)
    #     print up
    #     return render(request,'changepass.html',{ 'user':up })


def hospitalHome(request):
	if request.user.is_authenticated():
		a = hospital.objects.get(user_id = request.user)
		print a
		context = {
		"hos_details":a
		}

		return render(request,'hospitalHome.html',context)
	else:
		return redirect('/login/')	


def addDoctors(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			name = request.POST['doctorname']
			gender = request.POST['gender']
			speciality = request.POST['speciality']
			phone = request.POST['phone']
			email = request.POST['email']
			address = request.POST['address']
			workexp = request.POST['workexp']
			degree = request.POST['degree']
			salary = request.POST['salary']
			photo = request.FILES['profile_pic']

			

			hash = hashlib.sha1()
			now = datetime.datetime.now()
			hash.update(str(now)+email+'game_of_thrones')
			tp=hash.hexdigest()


			a = hospital.objects.get(user_id = request.user)
			print a
			user=User.objects.create(username=email,password=tp)
			user.save()

			doc = doctor.objects.create(d_name = name,d_email = email,d_phone_no = phone,d_address = address,d_spec = speciality,d_work_exp = workexp,d_degree = degree,d_salary = salary,d_gender = gender,user_id = user,d_hospital_id = a,profile_pic = photo)
			doc.save()

			utype = user_type.objects.create(user_detail=user,types=2)
			utype.save()
      


			# fromaddr=usermail
			# toaddr=email
			# msg=MIMEMultipart()
			# msg['From']=fromaddr
			# msg['To']=toaddr
			# msg['Subject']='Confirmational Email'
			# domain = request.get_host()
			# scheme = request.is_secure() and "https" or "http"
			# body = "Please Click On The Link To complete registration: {0}://{1}/{2}/changepass".format(scheme,domain,tp) 
			# part1 = MIMEText(body, 'plain')
			# msg.attach(MIMEText(body, 'plain'))
			# server = smtplib.SMTP('smtp.gmail.com', 587)
			# server.starttls()
			# server.login(fromaddr, upassword)
			# text = msg.as_string()
			# server.sendmail(fromaddr, toaddr, text)
			# server.quit()

			return HttpResponse('Check your mail box to confirm')
			
		else:
			a = hospital.objects.get(user_id = request.user)
			print a
			context = {
			"hos_details":a
			}

			return render(request,'addDoctors.html',context)	

def addPatients(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			print request.POST['dateofbirth']
			name = request.POST['patientname']
			dob = request.POST['dateofbirth']
			age = request.POST['age']
			gender = request.POST['gender']
			phone = request.POST['phone']
			email = request.POST['email']
			address = request.POST['address']
			bloodgrp = request.POST['selectbg']
			doc = request.POST.getlist('doctor[]')
			print "asdasdas",doc

			photo = request.FILES['profile_pic']			

			hash = hashlib.sha1()
			now = datetime.datetime.now()
			hash.update(str(now)+email+'game_of_thrones')
			tp=hash.hexdigest()


			a = hospital.objects.get(user_id = request.user)
			print a
			user=User.objects.create(username=email,password=tp)
			user.save()
			pat = patient.objects.create(
								p_name = name,
								p_age = age,
								p_gender = gender,
								p_phone_no = phone,
								p_email = email,
								p_address = address,
								p_dateofbirth = dob,
								p_bloodgrp = bloodgrp,
								# p_doctor = doctor,
								user_id = user,
								hospital_id = a,
								profile_pic = photo)
			for i in doc:
				d = doctor.objects.get(id = i)
				pat.doctor_id.add(d)
			pat.save()
			utype = user_type.objects.create(user_detail=user,types=3)
			utype.save()
      


			# fromaddr=usermail
			# toaddr=email
			# msg=MIMEMultipart()
			# msg['From']=fromaddr
			# msg['To']=toaddr
			# msg['Subject']='Confirmational Email'
			# domain = request.get_host()
			# scheme = request.is_secure() and "https" or "http"
			# body = "Please Click On The Link To complete registration: {0}://{1}/{2}/changepass".format(scheme,domain,tp) 
			# part1 = MIMEText(body, 'plain')
			# msg.attach(MIMEText(body, 'plain'))
			# server = smtplib.SMTP('smtp.gmail.com', 587)
			# server.starttls()
			# server.login(fromaddr, upassword)
			# text = msg.as_string()
			# server.sendmail(fromaddr, toaddr, text)
			# server.quit()

			return HttpResponse('Check your mail box to confirm')
			
		else:
			a = hospital.objects.get(user_id = request.user)
			print a
			doc = doctor.objects.filter(d_hospital_id = a)
			context = {
			"hos_details":a,
			"doctors" : doc
			}

			return render(request,'addPatients.html',context)	



def addLabHead(request):
	if request.user.is_authenticated():
		if request.method == 'POST':	
			name = request.POST['lhname']
			age = request.POST['age']
			gender = request.POST['gender']
			phone = request.POST['phone']
			email = request.POST['email']
			address = request.POST['address']
			salary = request.POST['salary']
			hash = hashlib.sha1()
			now = datetime.datetime.now()
			hash.update(str(now)+email+'game_of_thrones')
			tp=hash.hexdigest()			
			a = hospital.objects.get(user_id = request.user)
			user=User.objects.create(username=email,password=tp)
			user.save()
			lh = labhead.objects.create(
								l_name = name,
								l_age = age,
								l_gender = gender,
								l_number = phone,
								l_email = email,
								l_salary = salary,
								user_id = user,
								hospital_id = a)
			lh.save()
			utype = user_type.objects.create(user_detail=user,types=4)
			utype.save()
			# fromaddr=usermail
			# toaddr=email
			# msg=MIMEMultipart()
			# msg['From']=fromaddr
			# msg['To']=toaddr
			# msg['Subject']='Confirmational Email'
			# domain = request.get_host()
			# scheme = request.is_secure() and "https" or "http"
			# body = "Please Click On The Link To complete registration: {0}://{1}/{2}/changepass".format(scheme,domain,tp) 
			# part1 = MIMEText(body, 'plain')
			# msg.attach(MIMEText(body, 'plain'))
			# server = smtplib.SMTP('smtp.gmail.com', 587)
			# server.starttls()
			# server.login(fromaddr, upassword)
			# text = msg.as_string()
			# server.sendmail(fromaddr, toaddr, text)
			# server.quit()
			return HttpResponse('Check your mail box to confirm')
		else:
			a = hospital.objects.get(user_id = request.user)
			context = {
			"hos_details":a
			}
			return render(request,'addLabHead.html',context)	

def addCashier(request):
	if request.user.is_authenticated():
		if request.method == 'POST':	
			name = request.POST['lhname']
			age = request.POST['age']
			gender = request.POST['gender']
			phone = request.POST['phone']
			email = request.POST['email']
			address = request.POST['address']
			salary = request.POST['salary']
			hash = hashlib.sha1()
			now = datetime.datetime.now()
			hash.update(str(now)+email+'game_of_thrones')
			tp=hash.hexdigest()			
			a = hospital.objects.get(user_id = request.user)
			user=User.objects.create(username=email,password=tp)
			user.save()
			c = cashier.objects.create(
								c_name = name,
								c_age = age,
								c_gender = gender,
								c_number = phone,
								c_email = email,
								c_salary = salary,
								user_id = user,
								hospital_id = a)
			c.save()
			utype = user_type.objects.create(user_detail=user,types=5)
			utype.save()
			# fromaddr=usermail
			# toaddr=email
			# msg=MIMEMultipart()
			# msg['From']=fromaddr
			# msg['To']=toaddr
			# msg['Subject']='Confirmational Email'
			# domain = request.get_host()
			# scheme = request.is_secure() and "https" or "http"
			# body = "Please Click On The Link To complete registration: {0}://{1}/{2}/changepass".format(scheme,domain,tp) 
			# part1 = MIMEText(body, 'plain')
			# msg.attach(MIMEText(body, 'plain'))
			# server = smtplib.SMTP('smtp.gmail.com', 587)
			# server.starttls()
			# server.login(fromaddr, upassword)
			# text = msg.as_string()
			# server.sendmail(fromaddr, toaddr, text)
			# server.quit()
			return HttpResponse('Check your mail box to confirm')
		else:
			a = hospital.objects.get(user_id = request.user)
			context = {
			"hos_details":a
			}
			return render(request,'addLabHead.html',context)	

def all_patients(request):
	patients = patient.objects.all()
	context = {
		'patients' : patients
	}
	return render(request, 'all_patients.html', context)

def all_doctors(request):
	doctors = doctor.objects.all()
	context = {
		'doctors' : doctors
	}
	return render(request, 'all_doctors.html', context)

