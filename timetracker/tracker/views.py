from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import TimeBlock, Activity


class TimeBlockCreateView(CreateView):
    model = TimeBlock
    fields = ["activity", "duration"]


class ActivityCreateView(CreateView):
    model = Activity
    fields = ["name"]
