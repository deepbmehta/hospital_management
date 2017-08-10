from django.conf.urls import url
from patient import views
urlpatterns = [
	url(r'^search/', views.search),	
	url(r'^appointment/', views.appointment),	
	url(r'^blood_bank/', views.bloodBank),
	
]