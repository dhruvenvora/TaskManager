from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from . models import Tasks


# Create your views here.
def index(request):
	return render(request, 'Task/index.html')

def addtask(request):
	if request.method == 'POST':
		post_text = request.POST.get('the_post')
		response_data = {}

		response_data['result'] = 'Create post successful!'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)