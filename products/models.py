from django.db import models


class Production(models.Model):
    name = models.CharField(max_length=200, default=0)
    sizes = models.CharField(max_length=200, default=0)
    price = models.IntegerField(default=0)
    price_old = models.IntegerField(default=0)
    production_id = models.CharField(max_length=6, default=0)
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