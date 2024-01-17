from django.urls import path, re_path    #re_path -удаляет слеш
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="url-home"),
]