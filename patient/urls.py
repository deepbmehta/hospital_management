from django.conf.urls import url
from patient import views
urlpatterns = [
	

	url(r'^blood_bank/', views.bloodBank),
	
]