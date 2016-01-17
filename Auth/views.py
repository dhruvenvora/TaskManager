from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Users, Authentication
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	context = RequestContext(request, {'useridLabel':'Username:', 'passwordLabel':'Password:'})
	return render(request, 'Auth/index.html', context)
		
def login(request):
	return render(request, 'Auth/login.html')

def details(request):
	referer_url = request.META.get('HTTP_REFERER') #HTTP_REFERER contains the URL of the calling view.
	if referer_url is not None:
		if 'login' in referer_url:
			userid = request.POST['username']
			password = request.POST['password']			
			userAuth = Authentication.objects.get(pk=userid)
			if(userAuth is not None and userAuth.password == password):
				#TODO instead of printing the string, redirect the page to Tasks/index
				return HttpResponse("You are logged in %s. " % userid)
			else:
				return HttpResponseRedirect(reverse('Auth:login'))
			
		elif 'signup' in referer_url:
			userid = request.POST['username']
			f_name = request.POST['firstname']
			l_name = request.POST['lastname']
			name = f_name + " " + l_name
			email = request.POST['email']
			password = request.POST['password']
			contact = request.POST['phone']
			
			value= None
			try:
				#TODO what is the performance impact of following code on million users?
				value = Users.objects.get(pk=userid)
			except Users.DoesNotExist:
				user = Users(userid,name,email,contact,'')
				userAuth = Authentication(userid, password)
				user.save()
				userAuth.save()
				#context = RequestContext(request, {'userid':user.name})
				#TODO response should be redirected to the Home/index
				#change referer URL
				#return render(request, 'Auth/login.html',context)
				return HttpResponseRedirect(reverse('Auth:login'))
			else:
				return HttpResponseRedirect(reverse('Auth:index'))
		else:
			return HttpResponseRedirect(reverse('Auth:index'))
	else:
		return HttpResponseRedirect(reverse('Auth:index'))