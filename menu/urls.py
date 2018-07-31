from django.conf.urls import url
from django.urls import include
from django.contrib.auth.views import logout
from . import views
from Django_Project import settings
from . import views

urlpatterns = [
    url(r'^$', views.menu, name='menu'),
    url(r"^logout/$", views.logout_view, name="logout"),
]
