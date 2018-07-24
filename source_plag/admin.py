from django.contrib import admin
from source_plag.models import Corpus, Original, Suspicious

admin.site.register(Corpus)
admin.site.register(Original)
admin.site.register(Suspicious)
