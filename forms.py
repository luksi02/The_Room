from django import forms

from .models import Room, Reservation


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class SearchRoomForm(forms.ModelForm):
    is_free_today = forms.BooleanField(initial=True)
    class Meta:
        model = Room
        fields = ["name", "capacity", "projector"]

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["date", "comment"]