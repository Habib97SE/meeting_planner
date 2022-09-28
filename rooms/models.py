from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=1)
    projector = models.BooleanField(default=False)
    floor = models.IntegerField(default=1)
    number = models.IntegerField(default=1001)
    location = models.CharField(max_length=200, default="")
    building = models.CharField(max_length=100, default="")
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name
