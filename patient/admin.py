# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import patient,appointment
# Register your models here.
admin.site.register(patient)
admin.site.register(appointment)

