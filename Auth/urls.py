
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/*$', views.index, name = 'index'),
	url(r'^details/*$', views.details, name = 'details'),
]