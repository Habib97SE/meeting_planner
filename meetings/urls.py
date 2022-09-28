from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.show_meeting_detail, name="show_meeting_detail"),
    path("", views.show_meetings, name="show_meetings"),
    path("new", views.new_meeting, name="new_meeting"),
    path("edit/", views.edit_meeting, name="edit_meeting"),
    path("delete/", views.delete_meeting, name="delete_meeting"),
    ]