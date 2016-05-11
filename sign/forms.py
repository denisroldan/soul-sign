from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Sign


class SignForm(ModelForm):
    class Meta:
        model = Sign
        fields = ['author', 'text', 'expires']
        labels = {
            'author': _('Author'),
        }
        help_texts = {
            'author': _("Sign's author"),
        }
        error_messages = {
            'text': {
                'max_length': _("Sign text is too long!"),
            },
        }
