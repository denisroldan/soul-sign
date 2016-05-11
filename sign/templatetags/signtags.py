from django import template

from sign.models import Sign

register = template.Library()


@register.simple_tag
def get_soul_sign_hero_message():
    return "There are {0} soul signs in our systems!".format(Sign.objects.all().count())
