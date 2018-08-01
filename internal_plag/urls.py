from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CorpusListView.as_view(), name='internal_plagiarism'),
    url(r'^internal/(?P<pk>\d+)$', views.CorpusDetailView.as_view(), name='int-show-corpus'),
    url(r'^internal/create$', views.CorpusCreateView.as_view(), name='int-create-corpus'),
    url(r'^internal/list$', views.CorpusListView.as_view(), name='int-list-corpus'),
    url(r'^internal/suspicious/create-new$', views.CreateSuspiciousView.as_view(), name='int-create-suspicious'),
    url(r'^internal/start-detection/$', views.start_detection, name='int-start-detection'),
    url(r'^internal/multistep/$', views.multistep_process, name='int-multistep')
]
