from django.conf.urls import url
from hospital_reg import views

urlpatterns = [
	url(r'^homepage/', views.hospitalHome),
	url(r'^login/$', views.login_site),
	url(r'^logout/$', views.logout_site),


]