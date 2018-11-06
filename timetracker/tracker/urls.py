from django.urls import path

from . import views

urlpatterns = [
	path("", views.TimeBlockCreateView.as_view(), name="add_time_block"),
	path("activity/", views.ActivityCreateView.as_view(), name="add_activity")
]
