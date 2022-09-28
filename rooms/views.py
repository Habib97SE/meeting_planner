from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.http import HttpResponse
from rooms.models import Room


# Create your views here.
def show_rooms(request):
    return render(request, "rooms/rooms.html", {
        "title": "Rooms",
        "rooms": Room.objects.all(),
        "meta_keywords": "Rooms, Meeting Rooms, Conference Rooms, Meeting Planner",
        "meta_description": "List of rooms available for meetings"
    })


def edit_room(request, id):
    room = get_object_or_404(Room, id=id)
    if request.method == "POST":
        room.name = request.POST["room_name"]
        room.floor = request.POST["room_floor"]
        room.number = request.POST["room_number"]
        room.save()
        return render(request, "rooms/rooms.html", {
            "room": room
        })
    else:
        if room is not None:
            return render(request, "rooms/editroom.html", {
                "message": "room found",
                "room": room
            })
        else:
            return render(request, "rooms/rooms.html", {
                "message": "Room not found!"
            })


RoomForm = modelform_factory(Room, exclude=[])


def new_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_rooms')
    else:
        form = RoomForm()
    return render(request, "rooms/newroom.html", {
        "title": "New Room",
        "form": form
    })


def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    return render(request, "rooms/deleteroom.html", {
        "room": room
    })
