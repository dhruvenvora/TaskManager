
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<userid>[a-zA-Z]+)/details$', views.details, name = 'details'),
]