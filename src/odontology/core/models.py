from django.db import models
from django.contrib.auth.models import User


class Day(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.name)


class Bill(models.Model):
    user = models.ForeignKey(User)
    paid = models.BooleanField(default=False)
    linode_file = models.FileField(
        upload_to='linode/', max_length=100, null=True, blank=True
    )
    text = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.user, self.text)
