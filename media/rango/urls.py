from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
	url(r'^$',views.index,name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)