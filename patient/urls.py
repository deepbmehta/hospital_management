from django.conf.urls import url
from patient import views
urlpatterns = [
	url(r'^search/', views.search)	


]