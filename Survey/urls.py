from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("object_data/", views.object_data, name="object_data"),
path("object_type/", views.object_type, name="object_type"),
path("results/", views.results, name="results"),
]
