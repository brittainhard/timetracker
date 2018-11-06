from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import TimeBlock, Activity
from .pie_chart import BokehPieChart


class TimeBlockCreateView(CreateView):
    model = TimeBlock
    fields = ["activity", "duration"]


class ActivityCreateView(CreateView):
    model = Activity
    fields = ["name"]


class BokehPieChartView(TemplateView):
    template_name = "tracker/pie_chart.html"

    def get_context_data(self, *args, **kwargs):
        chart = BokehPieChart()
        context = super().get_context_data(*args, **kwargs)
        context["today"] = chart.today
        return context
