from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("watch/<str:video_id>", views.watch, name="watch"),

    # path("channel/<str:channel_id>", views.view_channel, name="view_channel"),
    # path("playlist/<str:playlist_id>", views.view_playlist, name="view_playlist"),
    # path("search/<str:query>", views.search, name="search"),
    # https://www.youtube.com/watch?v=BgIgKcqPd4k
    # https://www.youtube.com/watch?v=TK6w8poGSkQ
    # https://www.youtube.com/watch?v=1zrtBqZeylo
]