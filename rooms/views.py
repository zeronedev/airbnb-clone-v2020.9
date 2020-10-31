from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):
    # print(dir(request.GET))
    page = request.GET.get("page", 1)  # str
    page = int(page or 1)  # int
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)  # 올림
    return render(
        request,
        "rooms/home.html",
        context={
            "potato": all_rooms,
            "page": page,  # 현재페이지
            "page_count": page_count,  # 전체페이지
            "page_range": range(1, page_count),  # 페이지 범위리스트
        },
    )
