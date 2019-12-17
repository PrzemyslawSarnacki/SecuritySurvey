from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("object_data/", views.object_data, name="object_data"),
path("object_type/", views.object_type, name="object_type"),
path("service_object/", views.service_object, name="service_object"),
path("private_object/", views.private_object, name="private_object"),
path("public_object/", views.public_object, name="public_object"),
path("results/", views.results, name="results"),
]
