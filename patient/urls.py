from django.conf.urls import url
from patient import views
urlpatterns = [
	url(r'^search/', views.search),	

	url(r'^blood_bank/', views.bloodBank),
	url(r'^payment/', views.payment),
	
]