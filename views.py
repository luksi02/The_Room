from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, request
from .models import Room, Reservation
from .forms import RoomForm, ReservationForm, SearchRoomForm
import datetime


def show_all_rooms(request):
    rooms = Room.objects.all()
    for room in rooms:
        reservation_dates = [reservation.date for reservation in room.reservation_set.all()]
        room.reserved = datetime.date.today() in reservation_dates

        """if datetime.date.today() in reservation_dates:
            is_reserved = "Reserved today"
        else:
            is_reserved = "Not reserved today"""
    return render(request, "the_room/the_room_index.html", {"room": Room.objects.all(), "room.reserved": room.reserved})

"""for room in Room.objects.all():
    id_ = Room.objects.get(id)
    if Reservation.objects.filter(room_id_id=id_, date=datetime.date.today):
        is_reserved = "Reserved today"""



def add_room(request):
    if request.method == "GET":
        return render(request, "the_room/add_room.html", {"form": RoomForm})
    else:
        room_form = RoomForm(request.POST)
        # print(room_form.data)
        # print(room_form.data["name"])
        if not room_form.data["name"]:
            return HttpResponse("Room name can't be blank")
        if Room.objects.filter(name=room_form.data["name"]).first():
            return HttpResponse("Room name already in use!")
        if int(room_form.data["capacity"]) < 1:
            return HttpResponse("Room cant have capacity less than 1!")
        if room_form.is_valid():
            room_form.save()
            return redirect(reverse("show_all_rooms"))
        return HttpResponse("Oops, it didn't work! thanks for crashing our system!")

def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    room.delete()
    return redirect(reverse("show_all_rooms"))

def room_details(request, id):
    room = get_object_or_404(Room, id=id)
    reservation = Reservation.objects.filter(room_id_id=id)
    return render(request, "the_room/room_details.html", {"room": room, "reservation": reservation})

def update_room(request,id):
    room = get_object_or_404(Room, id=id)
    if request.method == "GET":
        return render(request, "the_room/add_room.html", {"form": RoomForm(instance=room)})
    else:
        room_form = RoomForm(request.POST, instance=room)
        if room_form.is_valid():
            room_form.save()
            return redirect(reverse("show_all_rooms"))
    return HttpResponse("Something went wrong")

def reserve_room(request):
    if request.method == "GET":
        return render(request, "the_room/reserve_room.html", {"form": ReservationForm})

def search_room(request):
    if request.method == "GET":
        return render(request, "the_room/search_room.html", {"form": RoomForm})
    else:
        # room_form.data["reserved"] = ""
        room_form = RoomForm(request.POST)
        search_room_name = room_form.data.get('name', "")
        search_room_capacity = room_form.data.get('capacity', 1)
        search_room_projector = room_form.data.get('projector', False)
        search_room_reserved = room_form.data.get('reserved', False)
        results = Room.objects.all()
        results = results.filter(capacity__gte=search_room_capacity)
        #results = results.filter(name=search_room_name)
        if search_room_projector:
            results = results.filter(projector=True)
        if search_room_reserved:
            results = results.filter(reserved=False)



        return render(request, "the_room/the_room_index.html", {"room": results})
        #return HttpResponse("Oops, it didn't work! thanks for crashing our system!")
        """
        
        #print(room_form.data)
        #print(room_form.data["name"])
        # print(room_form.data["capacity"])"""

        """if room_form.data["name"] in room_form.data:
            search_room_name = room_form.data["name"]
        else:
            search_room_name = ""
        if room_form.data["capacity"] in room_form.data:
            search_room_capacity = int(room_form.data["capacity"])
        else:
            search_room_capacity = 100
        if room_form.data["projector"] in room_form.data:
            search_room_projector = room_form.data["projector"]
        else:
            search_room_projector = False
        if room_form.data["reserved"] in room_form.data:
            search_room_reserved = room_form.data["reserved"]
        else:
            search_room_reserved = False

        print(search_room_name)
        print(search_room_capacity)
        print(search_room_projector)
        print(search_room_reserved)
"""
        """search_room_capacity = if room_form.data["capacity"] else search_room_capacity = 0
        search_room_projector = room_form.data["projector"] else search_room_projector = False
        search_room_reserved = room_form.data["reserved"] else search_room_reserved = False
        print(search_room_name)
        print(search_room_capacity)
        print(search_room_projector)
        print(search_room_reserved)"""
        """return HttpResponse("Oops, it didn't work! thanks for crashing our system!")
    return HttpResponse("Oops, it didn't work! thanks for crashing our system!")"""

"""        if room_form.data["name"]:
            # print(room_form.data["projector"])
            print(room_form.data)
            # print(room_form.data["is_free_today"])
            #if room_form.data["projector"] == "on":
            if room_form.data["projector"] in room_form.data:
                if room_form.data["is_free_today"] == "on":
                    results = Room.objects.filter(capacity__gte=room_form.data["capacity"]).filter(projector=True)
                    print(results)
                    return render(request, "the_room/the_room_index.html", {"room": results})
                else:
                    results = Room.objects.filter(capacity__gte= room_form.data["capacity"]).filter(projector=True).filter(reserved=False)
                    print(results)
                    return render(request, "the_room/the_room_index.html", {"room": results})
            else:
                results = Room.objects.filter(capacity__gte= room_form.data["capacity"])
                print(results)
                return render(request, "the_room/the_room_index.html", {"room": results})

        return HttpResponse("Oops, it didn't work! thanks for crashing our system!")"""


def reserve_room_1(request, id):
    reservation = get_object_or_404(Room, id=id)
    reservations = Reservation.objects.filter(room_id_id=id)
    if request.method == "GET":
        return render(request, "the_room/reserve_room.html", {"form": ReservationForm(instance=reservation), "reservations": reservations})
    else:
        reservation_form = ReservationForm(request.POST)
        if Reservation.objects.filter(room_id = id, date = reservation_form.data["date"]):
            return HttpResponse("There's already reservartion!")
        if reservation_form.data["date"] < str(datetime.date.today()):
            return HttpResponse("Invalid date - it already passed!")

        Reservation.objects.create(room_id_id=id, date=reservation_form.data["date"], comment=reservation_form.data["comment"])
        return redirect(reverse("show_all_rooms"))
        """if reservation_form.is_valid():
            reservation_form.save()
            return redirect(reverse("show_all_rooms"))"""
        # return HttpResponse("Oops, it didn't work! thanks for crashing our system!")
        """ if Room.objects.filter(name=room_form.data["name"]).first():
            return HttpResponse("Room name already in use!")
        if int(room_form.data["capacity"]) < 1:
            return HttpResponse("Room cant have capacityl less than 1!")
        if room_form.is_valid():
            room_form.save()
            return redirect(reverse("show_all_rooms"))
        return HttpResponse("Oops, it didn't work! thanks for crashing our system!")"""


# Create your views here.
