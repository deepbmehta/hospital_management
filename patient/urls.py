from django.conf.urls import url
from patient import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	url(r'^search/', views.search),	
	url(r'^appointment/', views.appointment),	
	url(r'^blood_bank/', views.bloodBank),
	url(r'^payment/', views.payment),
	url(r'^patientHome/', views.patientHome),
	url(r'^chat/', views.chat),
	url(r'^reports/', views.report),


	
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

	