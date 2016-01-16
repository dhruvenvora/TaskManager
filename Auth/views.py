from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Users
from django.core.urlresolvers import reverse

# Create your views here.
def index(request,isRedirect):
		context = RequestContext(request, {'useridLabel':'Username:', 'passwordLabel':'Password:', 'type':isRedirect})
		return render(request, 'Auth/index.html', context)

def details(request):
	userid = request.POST['username']
	f_name = request.POST['firstname']
	l_name = request.POST['lastname']
	name = f_name + " " + l_name
	email = request.POST['email']
	passwrd = request.POST['password']
	user = Users(userid,name,email,'1234','dhaval.jpg')
	value = None
	try:
		value = Users.objects.get(pk=userid)
	except Users.DoesNotExist:
		user.save()
		return HttpResponse("Hello %s" % user)	
	else:
		return HttpResponseRedirect(reverse('Auth:index',args = ['True',]))
	