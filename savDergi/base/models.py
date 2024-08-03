from django.db import models
from django.utils.text import slugify


class Duyuru(models.Model):
    topic = models.CharField(max_length=200)
    text = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.topic
