from django.contrib import admin
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText

admin.site.register(Album)
admin.site.register(Image)
admin.site.register(EmbeddedVideo)


@admin.register(DuyuruImage)
class DuyuruImageAdmin(admin.ModelAdmin):
    list_display = ("topic", "image", "created")


class DuyuruImageInline(admin.TabularInline):
    model = DuyuruImage
    extra = 1
    min = 0
    max_num = 50
    fields = ('image',)


@admin.register(DuyuruText)
class DuyuruTextAdmin(admin.ModelAdmin):
    list_display = ("topic", "text", "created")


class DuyuruTextInline(admin.TabularInline):
    model = DuyuruText
    extra = 1
    min = 1
    max_num = 50
    fields = ('text',)



@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):
    inlines = [DuyuruTextInline, DuyuruImageInline]


