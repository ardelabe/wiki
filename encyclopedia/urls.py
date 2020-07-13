from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("wiki", views.wiki, name="wiki"),
    path("results", views.wiki, name="results"),
]
