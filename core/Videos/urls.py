from django.urls import path
from . import views

urlpatterns = [
                  path("", views.home, name="home"),
                  path("home/", views.home, name="home"),
                  path("profile/<str:username>", views.profile, name="profile"),
                  path("watch/<str:video_id>", views.watch, name="watch"),

              < iframe;
width = "1352";
height = "624";
src = "https://www.youtube.com/embed/TK6w8poGSkQ";
title = "YouTube video player";
frameborder = "0";
allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen > </iframe >

# path("channel/<str:channel_id>", views.view_channel, name="view_channel"),
# path("playlist/<str:playlist_id>", views.view_playlist, name="view_playlist"),
# path("search/<str:query>", views.search, name="search"),
]
