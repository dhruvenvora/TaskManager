from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<userid>[a-zA-Z0-9]+)/$', views.index, name = 'index'),
	url(r'^addtask/*$', views.addtask, name = 'addtask'),
	url(r'^(?P<userid>[a-zA-Z0-9]+)/(?P<taskid>[a-zA-Z0-9:])/delete/*$', views.delete, name = 'delete'),
]

