from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Tasks


# Create your views here.
def index(request):
	return render(request, 'Task/index.html')

def addtask(request):
	taskid = '5'
	title = request.POST['title']
	description = request.POST['description']
	start_date = request.POST['start_date']
	due_date = request.POST['due_date']
	set_reminder_before = request.POST['time_counter']
	repeat = request.POST['repeat_checkbox']
	task = Tasks(taskid,title,description,start_date,due_date,repeat,set_reminder_before)
	task.save()
	return HttpResponse('Task added')