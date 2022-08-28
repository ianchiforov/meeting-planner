from django.db import models
from datetime import time


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=60)
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"Room {self.name} ({self.number}) on the floor {self.floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.title} at {self.start_time} on {self.date} "
                f"for {self.duration} hours")
