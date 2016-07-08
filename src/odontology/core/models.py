from django.db import models
from django.contrib.auth.models import User

class Bill(models.Model):
    user = models.ForeignKey(User)
    paid = models.BooleanField(default=False)
    url_file = models.URLField(max_length=150, null=True, blank=True)
    text = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.user, self.text)
