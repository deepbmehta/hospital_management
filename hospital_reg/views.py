# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospital_reg.models import *
from django.contrib.auth import authenticate,login,logout

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

