from django.forms import ModelForm
from .models import Sign


class SignForm(ModelForm):
    class Meta:
        model = Sign
        fields = ['author', 'text', 'expired']
