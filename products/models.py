from django.db import models
from django import forms

import json


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


class search_form(forms.Form):
    # Search field
    q = forms.CharField(label='Type to find: ', max_length=100, required=False)
    # Highest price field
    hi = forms.IntegerField(label='Highest price limit: ', initial=10000, min_value=0, required=False)
    # Lowest price field
    lo = forms.IntegerField(label='Lowest price limit: ', initial=1, min_value=0, required=False)
    # Kids field
    k = forms.BooleanField(label='Include kids models?: ', required=False)
    # Adult field
    a = forms.BooleanField(label='Include teen models? ', required=False)
    # Women field
    w = forms.BooleanField(label='Include women models?: ', required=False)
