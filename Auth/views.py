from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Users
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	context = RequestContext(request, {'useridLabel':'Username:', 'passwordLabel':'Password:'})
	return render(request, 'Auth/index.html', context)
		
def login(request):
	context = RequestContext(request)
	return render(request, 'Auth/login.html', context)

def details(request):
	referer_url = request.META.get('HTTP_REFERER') #HTTP_REFERER contains the URL of the calling view.
	if referer_url is not None:
		if 'login' in referer_url:
			userid = request.POST['username']
			passwrd = request.POST['password']
			#TODO instead of printing the string, redirect the page to Tasks/index
			return HttpResponse("You are logged in %s. " % userid)
		elif 'signup' in referer_url:
			userid = request.POST['username']
			f_name = request.POST['firstname']
			l_name = request.POST['lastname']
			name = f_name + " " + l_name
			email = request.POST['email']
			passwrd = request.POST['password']
			user = Users(userid,name,email,'1234','dhaval.jpg')
			value= None
			try:
				value = Users.objects.get(pk=userid)
			except Users.DoesNotExist:
				user.save()
				context = RequestContext(request, {'userid':user.name})
				return render(request, 'Auth/details.html',context)	
			else:
				return HttpResponseRedirect(reverse('Auth:index'))
	else:
		return HttpResponseRedirect(reverse('Auth:index'))