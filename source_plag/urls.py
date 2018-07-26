from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CorpusListView.as_view(), name='source_plagiarism'), #DEFAULT HOME PAGE
    url(r'^(?P<pk>\d+)$', views.CorpusDetailView.as_view(), name='show-corpus'),
    url(r'^create$', views.CorpusCreateView.as_view(), name='create-corpus'),
    url(r'^list$', views.CorpusListView.as_view(), name='list-corpus'),
    url(r'original/create-new', views.CreateOriginalView.as_view(), name='create-original'),
    url(r'suspicious/create-new', views.CreateSuspiciousView.as_view(), name='create-suspicious'),
]
