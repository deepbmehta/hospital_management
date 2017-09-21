from django.conf.urls import url
from hospital_reg import views

urlpatterns = [
	url(r'^homepage/', views.homepage),
	url(r'^login/$', views.login_site),
	url(r'^logout/$', views.logout_site),
	url(r'^hos_reg/$', views.hos_reg),
	url(r'^(?P<p>[\w\-\_]+)/changepass/$', views.hos_reg_complete),
	url(r'^hospitalHome/$', views.hospitalHome),
	url(r'^addDoctors/$', views.addDoctors),
	url(r'^addPatients/$', views.addPatients),
	url(r'^addLabHead/$', views.addLabHead),
	url(r'^addCashier/$', views.addCashier),
	url(r'^all_patients/$', views.all_patients),
	url(r'^all_doctors/$', views.all_doctors),



]