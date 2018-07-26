from django.conf.urls import url

from Django_Project import settings
from . import views

urlpatterns = [
    url(r'^$', views.menu, name='menu'), #DEFAULT HOME PAGE
    url(r'^logout/$', views.logout, name='logout'),
]
