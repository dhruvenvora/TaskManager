from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Tasks
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your views here.
def index(request, userid):
	task_list = Tasks.objects.all()
	context = RequestContext(request, {'userid':userid,'task_list_label':task_list})
	return render(request, 'Task/index.html', context)

def addtask(request):
	taskid = timezone.now
	title = request.POST['title']
	description = request.POST['description']
	x = request.POST['start_date']
	start_date = x + ' 00:00:00'
	y = request.POST['due_date']
	due_date = y + ' 00:00:00'
	set_reminder_before = request.POST['time_counter']
	repeat = request.POST['repeat_checkbox']
	task = Tasks(taskid,title,description,start_date,due_date,repeat,set_reminder_before)
	task.save()
	return HttpResponseRedirect(reverse('Task:index', kwargs={'userid':request.POST['hidden_userid']}))