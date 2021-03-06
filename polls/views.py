# Create your views here.

from django.shortcuts import render_to_response
from polls.models import Poll
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render_to_response('polls/index.html', context)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % (poll_id,))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll <strong>%s</strong>." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % (poll_id,))

def redirect_to_polls(request):
	return HttpResponseRedirect('/polls/')