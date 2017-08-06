# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def bloodBank(request):
	with open('patient/bloodbank.json', 'r') as f:
		hdata = json.load(f)
		print hdata
	return render(request,'bloodBank.html',hdata)
