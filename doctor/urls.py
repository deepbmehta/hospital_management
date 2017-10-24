from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from doctor import views
urlpatterns = [
	url(r'^confirm_appointments/$', views.confirm_appointments),
	url(r'^docHome/$', views.docHome),
	url(r'^confirm/$', views.confirm),
	url(r'^delete_appointment/$', views.delete_appointment),
	url(r'^docpatients/(?P<d_id>\d+)$', views.docpatients),
	url(r'^reportdocview/(?P<d_id>\d+)$', views.reportdocview),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
