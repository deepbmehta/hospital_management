from django.conf.urls import url
from hospital_reg import views

urlpatterns = [
	url(r'^', views.hospitalHome),


]