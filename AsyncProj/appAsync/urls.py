from django.urls import path
from . import views

urlpatterns = [
    path('', views.AsyncPage.as_view())
]