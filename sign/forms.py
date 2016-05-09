from django.forms import ModelForm
from .models import Sign


class SignForm(ModelForm):
    class Meta:
        model = Sign
        fields = ['author', 'text', 'expires']
        labels = {
            'author': 'Autor',
        }
        help_texts = {
            'author': 'El autor de la nota',
        }
        error_messages = {
            'text': {
                'max_length': "¡La nota es demasiado larga!",
            },
        }
