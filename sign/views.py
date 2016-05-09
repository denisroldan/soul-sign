from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.template import loader

from .models import Sign
from .forms import SignForm


def hello_world(request):
    return HttpResponse('Hello Talentum!')


@login_required
def list_signs(request):
    if request.user.is_superuser:
        all_signs = Sign.objects.all()
    else:
        all_signs = Sign.objects.filter(author=request.user)
    template = loader.get_template('sign_list.html')
    context = {'signs': all_signs}
    return HttpResponse(template.render(context, request))


def sign_detail(request, id):
    template = loader.get_template('sign_detail.html')
    obj = get_object_or_404(Sign, id=id)
    context = {'sign': obj}
    return HttpResponse(template.render(context, request))


# @login_required
def create_sign_form(request):
    template = loader.get_template('sign_create.html')
    if request.method == 'GET':
        form = SignForm()
        context = {'form': form,}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_sign', form.instance.id)
        else:
            return HttpResponse(template.render({'form': form,}, request))

    return HttpResponseBadRequest("ERROR!!")


def edit_sign_form(request, id):
    sign_obj = get_object_or_404(Sign, id=id)
    if request.method == 'GET':
        form = SignForm(instance=sign_obj)
        template = loader.get_template('sign_edit.html')
        context = {'form': form, 'sign': sign_obj}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        form = SignForm(request.POST, instance=sign_obj)
        if form.is_valid():
            form.save()
            return redirect('detail_sign', sign_obj.id)
    return HttpResponseBadRequest("ERROR!!")
