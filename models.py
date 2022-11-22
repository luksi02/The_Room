from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField(default=100)
    projector = models.BooleanField(default=True)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'date')


# Create your models here.
