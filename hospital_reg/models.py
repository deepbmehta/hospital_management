# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_type(models.Model):
    types = models.IntegerField()
    user_detail = models.ForeignKey(User)
    

    def __str__(self):
        return str(self.types)