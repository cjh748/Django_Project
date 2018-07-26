from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse


class Corpus(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    corpus_name = models.CharField(max_length=50, unique=True)


    def get_absolute_url(self):
        return reverse('show-corpus', kwargs={'pk': self.pk})

    def __str__(self):
        return self.corpus_name


class Original(models.Model):
    corpus = models.ForeignKey(Corpus, on_delete=CASCADE)
    original_file_name = models.CharField(max_length=50)
    original_file = models.FileField()

    def __str__(self):
        return self.original_file_name


class Suspicious(models.Model):
    corpus = models.ForeignKey(Corpus, on_delete=CASCADE)
    suspicious_file_names = models.CharField(max_length=50, unique=True)
    suspicious_file = models.FileField()

    def __str__(self):
        return self.suspicious_file_names

