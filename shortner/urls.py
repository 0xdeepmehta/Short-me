from django.contrib import admin
from django.urls import path
from . import views
from .models import Url
from .views import UrlView
from django.db import OperationalError


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('generate', views.generate, name='generate'),
]

try:
	urls = Url.objects.all()
	for i in urls:
		urlpatterns.append(path(i.url_id, UrlView.as_view(url=i.url)))

	def addUrlsFromDb(url):
	    urlpatterns.append(path(url.url_id, UrlView.as_view(url=url.url)))
except OperationalError:
	pass