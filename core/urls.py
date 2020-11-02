from django.urls import path
from rooms import views as room_views

app_name = "core"  # config > urls.py 의 namespace와 같아야한다

urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
