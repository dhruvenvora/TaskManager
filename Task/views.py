from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Tasks
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your views here.
def index(request, userid):
	task_list = Tasks.objects.all()
	y = sorted(task_list, key=lambda task: task.start_date, reverse  =True)
	context = RequestContext(request, {'userid':userid,'task_list_label':y})
	return render(request, 'Task/index.html', context)

def addtask(request):
	title = request.POST['title']
	description = request.POST['description']
	x = request.POST['start_date']
	start_date = x + ' 00:00:00'
	y = request.POST['due_date']
	due_date = y + ' 00:00:00'
	set_reminder_before = request.POST['time_counter']
	repeat = request.POST['repeat_checkbox']
	task = Tasks(title=title,description=description,start_date=start_date,due_date=due_date,repeat=repeat,set_reminder_before=set_reminder_before)
	task.save()
	return HttpResponseRedirect(reverse('Task:index', kwargs={'userid':request.POST['hidden_userid']}))

def delete(request,userid, taskid):
	Tasks.objects.filter(id =taskid).delete()
	return HttpResponseRedirect(reverse('Task:index', kwargs={'userid':userid}))
	