# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from django.http import HttpResponse
import urllib, json
from django.contrib.auth.models import User
from hospital_reg.models import *
from patient.models import *
from doctor.models import *
from labhead.models import *
from cashier.models import *
from patient.models import appointment



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search(request):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 3:
			p = patient.objects.get(user_id = request.user)



			if request.method == 'POST':
				name = request.POST['name']
				types = request.POST['type']
				url = "https://api.betterdoctor.com/2016-03-01/doctors?first_name="+name+"&specialty_uid="+types+"&location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&sort=full-name-asc&skip=0&limit=10&user_key=056686b82961deed0c023cc2de74ce3f"
				response = urllib.urlopen(url)
				data = json.loads(response.read())
				print data['data'][0]['insurances']
				for item in data['data']:
					print "Fsdfsdfsdfsdfsdfsdf"
					del item['insurances']
					print item
				
					
				context = {
				"data":data['data'],
				"p_details":p,

				"v":True
				} 
				return render(request,'search.html',context)
			else:		
				context = {
				
				"p_details":p,

				"v":False
				}
				return render(request,'search.html',context)



def bloodBank(request):
	if request.user.is_authenticated():
		with open('patient/bloodbank.json', 'r') as f:
			hdata = json.load(f)
			all = hdata['data']
		page = request.GET.get('page', 1)
		p = patient.objects.get(user_id = request.user)
		print p

		
		paginator = Paginator(all, 92)
		try:
			a = paginator.page(page)
		except PageNotAnInteger:
			a = paginator.page(1)
		except EmptyPage:
			a = paginator.page(paginator.num_pages)
		context = {
		"p_details":p,
		"a":a,

		}	
		return render(request,'bloodBank.html',context)
	else:
		return redirect('/login/')	


def payment(request):
	if request.user.is_authenticated():
		p = patient.objects.get(user_id = request.user)
		print p
		c = invoice.objects.filter(p_id = p)
		print c
		context = {
		"p_details":p,
		"invoice":c
		}
		return render(request,'payment.html',context)	
	else:
		return redirect('/login/')	

def patientHome(request):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 3:
			p = patient.objects.get(user_id = request.user)
			print p

			context = {
			"p_details":p

			}

			return render(request,'patientHome.html',context)
		else:
			return HttpResponse("You are not allowed")
	else:
		return redirect('/login/')	

def chat(request):
	p = patient.objects.get(user_id = request.user)
	print p.hospital_id
	d = doctor.objects.filter(d_hospital_id = p.hospital_id)
	print d


	context = {
	"p_details":p,
	"d_list":d,
	}
	return render(request,'chat.html',context)

def report(request):
	if request.user.is_authenticated():
		p = patient.objects.get(user_id = request.user)
		print p
		
		rep = reports.objects.filter(p_id = p)
		context = {
		"p_details":p,
		"reports":rep
		}
		return render(request,'reports.html',context)
	else:
		return redirect('/login/')	


def book_app(request):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 3:
			p = patient.objects.get(user_id = request.user)
			print p
			doc = doctor.objects.filter(d_hospital_id = p.hospital_id)
			print doc
			if request.method == 'POST':
				date = request.POST['dateofappointment']
				fromtime = request.POST['fromtime']
				totime = request.POST['totime']
				cons_doc = doctor.objects.get(id = request.POST['doctor'])
				cond = request.POST['condition']
				note = request.POST['note']


				print date,fromtime,totime,cons_doc,cond,note
				 
				appo = appointment.objects.create(date_of_appointment = date,
												from_time = fromtime,
												to_time = totime,
												cons_doctor = cons_doc,
												condition = cond,
												note = note,
												book_patient = p)
				appo.save()
				return redirect("/all_appointments/")

			context = {
			"p_details":p,
			"doc_list":doc

			}
	return render(request,'book_appointment.html',context)



def all_appointments(request):
	if request.user.is_authenticated():
		if user_type.objects.get(user_detail = request.user).types == 3:
			p = patient.objects.get(user_id = request.user)
			print p
			app = appointment.objects.filter(book_patient = p)
			print app


			context = {
			"p_details":p,
			"app":app
			}
			return render(request,'all_appointments.html',context)


