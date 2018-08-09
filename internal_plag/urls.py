from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CorpusListView.as_view(), name='internal_plagiarism'),
    url(r'^internal/(?P<pk>\d+)$', views.CorpusDetailView.as_view(), name='int-show-corpus'),
    url(r'^internal/create$', views.CorpusCreateView.as_view(), name='int-create-corpus'),
    url(r'^internal/list$', views.CorpusListView.as_view(), name='int-list-corpus'),
    url(r'^delete-suspicious-internal/$', views.delete_suspicious_internal, name='delete-suspicious-internal'),
    url(r'^internal/suspicious/create-new$', views.CreateSuspiciousView.as_view(), name='int-create-suspicious'),
    url(r'^internal/start-detection/$', views.start_detection, name='int-start-detection'),
    url(r'^multistep/$', views.multistep_process, name='int-multistep')
]
