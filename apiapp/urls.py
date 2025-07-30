from django.urls import path
from . import views



urlpatterns = [


    path("", views.attackareal),
    path("home/", views.attackareal),
    path("alluser/", views.UserView.as_view()),
    path("removeuser/<int:id>/", views.RemoveUser.as_view()),
    path("user/<int:id>/", views.FetchUser.as_view()),
]


