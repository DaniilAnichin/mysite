import datetime

from django.db import models
from django.utils import timezone


class friend(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=10)
    age = models.CharField(max_length=20)
    meeting_date = models.DateField('date of the 1st meeting', blank=True, default=timezone.now())

    def was_met_recently(self):
        return self.meeting_date >= timezone.now() - datetime.timedelta(days=365)

    was_met_recently.admin_order_field = 'meeting_date'
    was_met_recently.boolean = True
    was_met_recently.short_description = 'Was met recently?'

    def is_older(self):
        return self.age >= 16

    def __str__(self):
        return "%s (%s years)" % (self.name, self.age)


class location(models.Model):
    friend = models.ForeignKey(friend)
    location_text = models.CharField(max_length=200)
    arrivals_date = models.DateField('date arrived', null=True)
    departure_date = models.DateField('date departured', null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.location_text
