from django.urls import path

from . import views

urlpatterns = [
	path("", views.TimeBlockCreate.as_view(), name="add_time_block")
]
