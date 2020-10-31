from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)  # str
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)

    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
    # except PageNotAnInteger:
    #     return redirect("/")
    # except Exception:
    #     return redirect("/")
