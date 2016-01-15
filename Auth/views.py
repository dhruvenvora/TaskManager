from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext
from . models import Users

# Create your views here.
def index(request):
	context = RequestContext(request, {'useridLabel':'Username:', 'passwordLabel':'Password:',})
	return render(request, 'Auth/index.html', context)

def details(request):
	userid = request.POST['username']
	value = get_object_or_404(Users, pk=userid)
	return HttpResponse("Hello %s " % value)