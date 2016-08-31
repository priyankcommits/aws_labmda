from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Requests(models.Model):
    request_text = models.CharField(max_length=100)
