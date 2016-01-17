from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Tasks


# Create your views here.
def index(request):
	return render(request, 'Task/index.html')

def addtask(request):
	return render(request, 'Task/addtask.html')