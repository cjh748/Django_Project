import codecs

from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse


class Corpus(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name="internal_corpus")
    corpus_name = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('int-show-corpus', kwargs={'pk': self.pk})

    def __str__(self):
        return self.corpus_name


class Suspicious(models.Model):
    corpus = models.ForeignKey(Corpus, on_delete=CASCADE)
    suspicious_file_names = models.CharField(max_length=50, unique=True)
    suspicious_file = models.FileField()

    def display_text_file_sus(self):
        with codecs.open(self.suspicious_file.path, 'r', encoding='utf-8-sig', errors='ignore') as fp:
            return fp.read()

    def __str__(self):
        return self.suspicious_file_names

