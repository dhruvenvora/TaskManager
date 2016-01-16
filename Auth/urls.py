
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<isRedirect>[a-zA-Z]*)$', views.index, name = 'index'),
	url(r'^details$', views.details, name = 'details'),
]