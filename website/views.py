import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

from meetings.models import Meeting, Room

# Create your views here.

TEMPLATE_FOLDER = "website/"


def find_current_week_period():
    today = datetime.datetime.now()

    date_1 = datetime.datetime.strptime(today.strftime("%m/%d/%y"), "%m/%d/%y")

    current_week_remain_days = 6 - today.weekday()

    end_date = date_1 + datetime.timedelta(days=current_week_remain_days)
    return end_date


def homepage(request):
    all_meetings = Meeting.objects.all()
    current_week_meetings = {}
    current_week_period = find_current_week_period()
    for meeting in all_meetings:
        if meeting.date <= current_week_period:
            current_week_meetings[meeting.date] = meeting

    return render(request, TEMPLATE_FOLDER + "index.html", {
        "meta_keywords": "meeting planner, meeting, planner, meeting planner app, meeting planner website, meeting planner software",
        "meta_description": "Meeting Planner is a website that helps you to plan your meetings.",
        "title": "Homepage",
        "upcoming_meetings": current_week_meetings if current_week_meetings else "No upcoming meetings"
    })

def terms_of_service_page(request):
    return render(request, TEMPLATE_FOLDER + "terms_of_service.html", {
        "meta_keywords" : "terms of service, meeting planner terms, terms of use",
        "meta_description" : "Terms of service for Meeting Planner website.",
        "title": "Terms of Service"
    })
