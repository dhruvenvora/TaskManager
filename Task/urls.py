from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<	>[a-zA-Z0-9]+)/$', views.index, name = 'index'),
	url(r'^addtask/*$', views.addtask, name = 'addtask'),
]

