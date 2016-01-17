
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/*$', views.login, name = 'login'),
	url(r'^signup/*$', views.index, name = 'index'),
	url(r'^details/*$', views.details, name = 'details'),
]