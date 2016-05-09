from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Sign
from .forms import SignForm


def hello_world(request):
	return HttpResponse('Hello Talentum!')


# @login_required
def create_sign_form(request):
	if request.method == 'GET':
		form = SignForm()
		template = loader.get_template('create_sign.html')
		context = {'form': form,}
		return HttpResponse(template.render(context, request))
	elif request.method == 'POST':
		form = SignForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("OK!!")
	return HttpResponseBadRequest("ERROR!!")


def edit_sign_form(request, id):
	if request.method == 'POST' and request.user.is_authenticated():
		s = get_object_or_404(Sign, id=id)
		form = SignForm(request.POST, instance=s)
		if form.is_valid():
			form.save()
			return HttpResponse("OK!!")
	return HttpResponseBadRequest("ERROR!!")
