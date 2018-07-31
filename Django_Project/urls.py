from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^menu', include('menu.urls')),
    url(r'^source_plag/', include('source_plag.urls')),
    url(r'^internal_plag/', include('internal_plag.urls'))
]
