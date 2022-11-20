from django.urls import path

from api import views

urlpatterns = [
    path("", view=views.api_home)
]
