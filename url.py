from django.urls import path

from .views import (
    show_all_rooms,
    delete_room,
    add_room,
    update_room,
    room_details,
    reserve_room,
    reserve_room_1,
    search_room

)

urlpatterns = [
    path("show_all_rooms/", show_all_rooms, name="show_all_rooms"),
    path("add_room/", add_room, name="add_room"),
    path("search_room/", search_room, name="search_room"),
    path("update_room/<int:id>/", update_room, name="update_room"),
    path("delete_room/<int:id>/", delete_room, name="delete_room"),
    path("room_details/<int:id>/", room_details, name="room_details"),
    path("reserve_room", reserve_room, name="reserve_room"),
    path("reserve_room_1/<int:id>/", reserve_room_1, name="reserve_room_1"),
]