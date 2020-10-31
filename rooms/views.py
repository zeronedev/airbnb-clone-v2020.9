# from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page")  # str
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    # print(vars(rooms))
    # print(dir(rooms))
    # print(vars(rooms.paginator))
    return render(
        request,
        "rooms/home.html",
        {"rooms": rooms},
    )
