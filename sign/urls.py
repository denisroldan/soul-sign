from django.conf.urls import url
from .views import create_sign_form

urlpatterns = [
    url(r'^create/', create_sign_form, name="create_sign"),
]