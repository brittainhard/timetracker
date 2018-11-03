import datetime
from django.utils import timezone
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self, *args, **kwargs):
        return self.name


class Day(models.Model):
    date = models.DateField(default=datetime.date.today)


class TimeBlock(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    recorded_time = models.DateTimeField(default=timezone.now)

    def __str__(self, *args, **kwargs):
        return self.activity.name
