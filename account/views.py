from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate
from django.contrib.auth import login as django_login
from django.utils.translation import ugettext_lazy as _

from account.forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user and user.is_active:
                django_login(request, user)
                return redirect(request.GET.get('next', '/sign/'))
            else:
                form.add_error(None, _('Invalid username or password'))
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('account:login')
