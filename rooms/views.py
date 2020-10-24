# from datetime import datetime
# from django.http.request import HttpRequest
# from django.http.response import HttpResponse
from django.shortcuts import render


def all_rooms(request):
    # print(dir(request))
    # now = datetime.now()
    # return HttpResponse(content=f"<h1>{request.user}  {now}</h1>")
    return render(request, "all_rooms")
