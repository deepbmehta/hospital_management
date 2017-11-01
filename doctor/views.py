# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from hospital_reg.models import *
from patient.models import *
from doctor.models import *
from labhead.models import *
from cashier.models import *
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from hospital_reg.safe import usermail,upassword
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib




def reportdocview(request, d_id):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 2:
			d = doctor.objects.get(user_id = request.user)
			doc = doctor.objects.get(id=d_id)
			h_id = doc.d_hospital_id
			allp = patient.objects.filter(hospital_id=h_id)
			dp = []
			t = []
			for p in allp:
				for i in p.doctor_id.all():
					if doc.id == i.id:
						dp.append(p)
			pallr = [[] for i in range(len(dp))]
			i=0
			for p in dp:
				rep = reports.objects.filter(p_id = p)
				pallr[i].append(rep)
				i+=1
			zipped = zip(dp,pallr)
			context = {
				"doc":d,
				'zipped' : zipped,
				'pallr' : pallr
			}
			return render(request, 'reportdocview.html', context)
		else:
			return HttpResponse("You are not allowed")
	else:
		return redirect('/login/')	

def docpatients(request, d_id):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 2:
			d = doctor.objects.get(user_id = request.user)
			doc = doctor.objects.get(id=d_id)
			h_id = doc.d_hospital_id
			allp = patient.objects.filter(hospital_id=h_id)
			dp = []
			for p in allp:
				for i in p.doctor_id.all():
					if doc.id == i.id:
						dp.append(p)
			context = {
				"doc":d,
				'patients' : dp,
			}
			return render(request, 'docpatients.html', context)
		else:
			return HttpResponse("You are not allowed")
	else:
		return redirect('/login/')


# Create your views here.
def docHome(request):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 2:
			d = doctor.objects.get(user_id = request.user)
			print d

			context = {
			"doc":d
			}
			return render(request,'docHome.html',context)
		else:
			return HttpResponse("You are not allowed")
	else:
		return redirect('/login/')


def confirm_appointments(request):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 2:
			doc = doctor.objects.get(user_id = request.user)
			app = appointment.objects.filter(cons_doctor = doc)
			for i in app:
				print i.book_patient
			context = {
			"app":app,
			"doc":doc
			}
			return render(request,'confirm_appointments.html',context)
		else:
			return HttpResponse("Not allowed to access")
	else:
		return redirect('/login/')



@csrf_exempt
def confirm(request):
	a = json.loads(request.body)
	print a['id']
	app = appointment.objects.get(id = int(a['id']))
	app.confirm = True
	app.save()
	print app.book_patient.p_email
	fromaddr=usermail
	toaddr=app.book_patient.p_email
	msg=MIMEMultipart()
	msg['From']=fromaddr
	msg['To']=toaddr
	msg['Subject']='Confirmation of Appointment'
	domain = request.get_host()
	scheme = request.is_secure() and "https" or "http"
	body = "Your Appointment is confirmed" 
	part1 = MIMEText(body, 'plain')
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, upassword)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

	return JsonResponse({"success":"true"})


@csrf_exempt
def delete_appointment(request):
	a = json.loads(request.body)
	print a['id']
	app = appointment.objects.get(id = int(a['id']))
	fromaddr=usermail
	toaddr=app.book_patient.p_email
	msg=MIMEMultipart()
	msg['From']=fromaddr
	msg['To']=toaddr
	msg['Subject']='Cancelation of appointment '
	domain = request.get_host()
	scheme = request.is_secure() and "https" or "http"
	body = "Your Appointment is cancelled. Please Select another day and time" 
	part1 = MIMEText(body, 'plain')
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, upassword)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	app.delete()
	return JsonResponse({"success":"true"})







