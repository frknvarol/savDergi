from django.contrib import admin
from .models import Duyuru, Album, Image, EmbeddedVideo

admin.site.register(Duyuru)
admin.site.register(Album)
admin.site.register(Image)
admin.site.register(EmbeddedVideo)