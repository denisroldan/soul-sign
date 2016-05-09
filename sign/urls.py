from django.conf.urls import url
from .views import create_sign_form, list_signs, sign_detail, edit_sign_form

urlpatterns = [
    url(r'^$', list_signs, name="list_signs"),
    url(r'^(?P<id>[0-9]+)/$', sign_detail, name="detail_sign"),
    url(r'^(?P<id>[0-9]+)/edit/$', edit_sign_form, name="edit_sign"),
    url(r'^create/', create_sign_form, name="create_sign"),
]