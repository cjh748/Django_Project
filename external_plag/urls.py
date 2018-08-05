from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CorpusListView.as_view(), name='external_plagiarism'),
    url(r'^external/(?P<pk>\d+)$', views.CorpusDetailView.as_view(), name='ext-show-corpus'),
    url(r'^external/create$', views.CorpusCreateView.as_view(), name='ext-create-corpus'),
    url(r'^external/list$', views.CorpusListView.as_view(), name='ext-list-corpus'),
    url(r'^external/suspicious/create-new$', views.CreateSuspiciousView.as_view(), name='ext-create-suspicious'),
    url(r'^external/start-detection/$', views.start_detection, name='ext-start-detection'),
    url(r'^multistep/$', views.multistep_process, name='ext-multistep')
]
