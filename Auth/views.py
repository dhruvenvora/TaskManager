from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.
def index(request):
	template = loader.get_template("Auth/index.html")
	context = RequestContext(request, {'useridLabel':'Username:', 'passwordLabel':'Password:',})
	return HttpResponse(template.render(context))

def details(request, userid):
	return HttpResponse("Hello %s " % userid)