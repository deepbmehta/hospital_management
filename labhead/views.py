# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


from django.shortcuts import render
from hospital_reg.models import *
from doctor.models import *
from patient.models import *
from labhead.models import *
from cashier.models import *	
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def labHome(request):
	
	lh = labhead.objects.get(user_id = request.user)
	print lh
	patientlist = patient.objects.filter(hospital_id = lh.hospital_id)
	print patientlist
	context = {
	"patient" : patientlist 
	}
	return render(request, 'labHome.html',context)


def upload(request):
	if request.method == 'POST':
		us = request.POST['user_id']
		file = request.FILES['report']
		pa = patient.objects.get(id = us)
		print pa


		re = reports.objects.create(p_id = pa,report = file)
		return HttpResponse("dasdsa")
	else:
		pass

