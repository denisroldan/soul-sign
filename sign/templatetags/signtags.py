from django import template
from django.utils.translation import ugettext_lazy as _

from sign.models import Sign

register = template.Library()


@register.simple_tag
def get_soul_sign_hero_message():
    return _("There are {0} soul signs in our systems!").format(Sign.objects.all().count())
