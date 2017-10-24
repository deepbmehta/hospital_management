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
def cashierHome(request):
	
	lh = cashier.objects.get(user_id = request.user)
	print lh
	patientlist = patient.objects.filter(hospital_id = lh.hospital_id)
	print patientlist
	context = {
	"patient" : patientlist 
	}
	return render(request, 'cashierHome.html',context)


def makebill(request):
	if request.method == 'POST':
		ca = cashier.objects.get(user_id = request.user)
		us = request.POST['user_id']
		file = request.FILES['bill']
		amount = request.POST['amount']
		pa = patient.objects.get(id = us)
		print pa


		re = invoice.objects.create(p_id = pa,i_amount = amount,bills = file,hospital_id = ca.hospital_id)
		return HttpResponse("Bill uploaded Successfully")
	else:
		pass