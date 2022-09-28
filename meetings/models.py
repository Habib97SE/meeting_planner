from django.db import models
from datetime import time
from rooms.models import Room


# Create your models here.


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField(default=time(9, 0))
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    location = models.CharField(max_length=255)
    agenda = models.TextField(default="Add some agenda here")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        meeting_detail = {
            "title": self.title,
            "date": self.date,
            "time": self.time,
            "duration": self.duration,
            "location": self.location,
            "agenda": self.agenda,
            "room": self.room,
        }
        return meeting_detail
