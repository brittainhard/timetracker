from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import TimeBlock


class TimeBlockCreate(CreateView):
    model = TimeBlock
    fields = ["activity"]
