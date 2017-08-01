# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import user_type,hospital
# Register your models here.
admin.site.register(user_type)
admin.site.register(hospital)