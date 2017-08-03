# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospital_reg.models import *
from django.contrib.auth import authenticate,login,logout
import smtplib
import re
import hashlib
from email.MIMEMultipart import MIMEMultipart
from hospital_reg.safe import usermail,upassword
from email.MIMEText import MIMEText
import datetime


# Create your views here.
def hospitalHome(request):
	return render(request, 'index.html')


def login_site(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = username, password = password)

		if user:
			login(request, user)
			if user_type.objects.get(user_detail = request.user).types == 1:
				return HttpResponse("You are an hospital")
			if user_type.objects.get(user_detail = request.user).types == 2:
				return HttpResponse("You are a doctor")
			if user_type.objects.get(user_detail = request.user).types == 3:
				return HttpResponse("You are a patient")
			if user_type.objects.get(user_detail = request.user).types == 4:
				return HttpResponse("You are a Cashier")
			if user_type.objects.get(user_detail = request.user).types == 5:
				return HttpResponse("You are a Lab Head")				
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


def base(request):
	return render(request,'base.html')





	
