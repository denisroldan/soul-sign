from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Sign


class SignForm(ModelForm):
    class Meta:
        model = Sign
        fields = ['text', 'expires']
        labels = {
            'text': _('Texto'),
        }
        help_texts = {
            'text': _("Texto de la nota"),
        }
        error_messages = {
            'text': {
                'max_length': _("Sign text is too long!"),
            },
        }
