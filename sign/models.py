from django.contrib.auth.models import User
from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Sign(models.Model):
    author = models.ForeignKey(User)
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    expire_datetime = models.DateTimeField()

    def __str__(self):
        return "{0} created by {1} on {2}".format(self.text, self.author, self.timestamp)

    class Meta:
        verbose_name = "Soul Sign"
        verbose_name_plural = "Soul Signs"
