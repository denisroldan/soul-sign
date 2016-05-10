from django.conf.urls import url

from .views import login, logout

patterns = [
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
]
