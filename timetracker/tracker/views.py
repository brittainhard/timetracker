from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import TimeBlock, Activity
from .plots import PieChart


class TimeBlockCreateView(CreateView):
    model = TimeBlock
    fields = ["activity", "duration"]


class ActivityCreateView(CreateView):
    model = Activity
    fields = ["name"]


class PlotView(TemplateView):
    template_name = "tracker/plots.html"

    def get_context_data(self, *args, **kwargs):
        chart = PieChart()
        context = super().get_context_data(*args, **kwargs)
        context["today"] = chart.today
        context["past_week"] = chart.past_week
        return context
