from django.contrib.auth.models import User
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField


@python_2_unicode_compatible
class Sign(models.Model):
    author = models.ForeignKey(User, help_text=_("Soul sign's author"))
    location = GeopositionField()
    text = models.CharField(max_length=200, help_text=_("Description of the sign"))
    created = models.DateTimeField(auto_now_add=True, help_text=_("Creation time"))
    expires = models.DateTimeField(null=True, blank=True, help_text=_("Time to live"))

    def __str__(self):
        return _("{0} created by {1} on {2}").format(self.text, self.author, self.created)

    class Meta:
        verbose_name = _("Soul Sign")
        verbose_name_plural = _("Soul Signs")