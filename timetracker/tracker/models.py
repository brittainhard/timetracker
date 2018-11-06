import datetime
from django.utils import timezone
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return "/"

    def __str__(self, *args, **kwargs):
        return self.name


class TimeBlock(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    recorded_time = models.DateField(default=datetime.date.today)
    duration = models.DurationField(default=None)

    def get_absolute_url(self):
        return "/"

    def __str__(self, *args, **kwargs):
        return "%s, %s, %s" % (self.recorded_time, self.activity.name,
                self.duration)
