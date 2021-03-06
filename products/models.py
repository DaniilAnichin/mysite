from django.db import models
from django import forms

import json

try:
    # for python 2.*
    import urllib2
except:
    # for python 3.*
    import urllib.request


class production(models.Model):
    name = models.CharField(max_length=200, default=0)
    sizes = models.CharField(max_length=200, default=0)
    price = models.IntegerField(default=0)
    price_old = models.IntegerField(default=0)
    id = models.CharField(max_length=6, default=0, primary_key=True, unique=True)
    delivery = models.CharField(max_length=20, default=0)
    kids = models.BooleanField(default=False)
    kid_adult = models.BooleanField(default=False)
    free_porto = models.BooleanField(default=False)
    package = models.BooleanField(default=False)
    women = models.BooleanField(default=False)
    url = models.URLField(default=0)
    img_url = models.URLField(default=0)

    def __unicode__(self):
        return self.name