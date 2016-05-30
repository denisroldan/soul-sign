from datetimewidget.widgets import DateTimeWidget
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Sign


class SignForm(forms.ModelForm):
    # expires = forms.DateTimeField()

    class Meta:
        model = Sign
        fields = ['text', 'expires']
        labels = {
            'text': _('Text'),
        }
        help_texts = {
            'text': _("Sign text"),
        }
        error_messages = {
            'text': {
                'max_length': _("Sign text is too long!"),
            },
        }
        widgets = {
            'expires': DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True, bootstrap_version=2)
        }
