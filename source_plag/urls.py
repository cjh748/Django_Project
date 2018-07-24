from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.source_plagiarism, name='source_plagiarism'), #DEFAULT HOME PAGE
]
