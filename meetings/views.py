from multiprocessing import reduction
from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Meeting
from rooms.models import Room
from django.forms import modelform_factory


# Create your views here.


def show_meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {
        "meeting": meeting,
    })


def show_meetings(request):
    meetings = Meeting.objects.all()
    return render(request, "meetings/allmeetings.html", {
        "meetings": meetings,
    })


MeetingForm = modelform_factory(Meeting, exclude=[])


def new_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_meeting')
    else:
        form = MeetingForm()
    return render(request, "meetings/newmeeting.html", {
        "title": "New Meeting",
        "form": form
    })


def edit_meeting(request):
    return render(request, "meetings/editmeeting.html", {
        "title": "Edit Meeting",
    })


def delete_meeting(request):
    return render(request, "meetings/deletemeeting.html", {
        "title": "Delete Meeting",
    })
