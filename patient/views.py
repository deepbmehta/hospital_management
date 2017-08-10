# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect
from django.http import HttpResponse
import urllib, json
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search(request):
	if request.method == 'POST':
		name = request.POST['name']
		types = request.POST['type']
		url = "https://api.betterdoctor.com/2016-03-01/doctors?first_name="+name+"&specialty_uid="+types+"&location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&sort=full-name-asc&skip=0&limit=10&user_key=056686b82961deed0c023cc2de74ce3f"
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		print data['data']
		context = {
		"data":data['data']
		} 
		return render(request,'search.html',context)
	else:		
		return render(request,'search.html')

def bloodBank(request):
	with open('patient/bloodbank.json', 'r') as f:
		hdata = json.load(f)
		all = hdata['data']
	page = request.GET.get('page', 1)
	paginator = Paginator(all, 90)
	try:
		a = paginator.page(page)
	except PageNotAnInteger:
		a = paginator.page(1)
	except EmptyPage:
		a = paginator.page(paginator.num_pages)
	return render(request,'bloodBank.html',{"a":a})
