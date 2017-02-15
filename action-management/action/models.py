from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class ActionManagement(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    assigned_user = models.ForeignKey(User, related_name='assigned_user')

    def __unicode__(self):
        return self.title
