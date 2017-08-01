from django.conf.urls import url
from hospital_reg import views

urlpatterns = [
	url(r'^homepage/', views.hospitalHome),
	url(r'^login/$', views.login_site),
	url(r'^logout/$', views.logout_site),
	url(r'^hos_reg/$', views.hos_reg),
	url(r'^(?P<p>[\w\-\_]+)/changepass/$', views.hos_reg_complete)


]