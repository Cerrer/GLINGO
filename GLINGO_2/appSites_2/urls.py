from django.urls import path, re_path    #re_path -удаляет слеш
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="url-home"),
    re_path(r'news/?$', views.NewsPage.as_view(), name="url-news"),
    re_path(r'proposal/?$', views.ProposalPage.as_view(), name="url-proposal"),
    re_path(r'contacts/?$', views.ContactsPage.as_view(), name="url-contacts"),
]