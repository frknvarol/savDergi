from django.contrib import admin
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText

admin.site.register(EmbeddedVideo)
admin.site.register(Image)


@admin.register(DuyuruImage)
class DuyuruImageAdmin(admin.ModelAdmin):
    list_display = ("topic", "image", "created")


class DuyuruImageInline(admin.TabularInline):
    model = DuyuruImage
    extra = 1
    min = 0
    max_num = 50
    fields = ('image', 'ordering')


@admin.register(DuyuruText)
class DuyuruTextAdmin(admin.ModelAdmin):
    list_display = ("topic", "text", "created")


class DuyuruTextInline(admin.TabularInline):
    model = DuyuruText
    extra = 1
    min = 1
    max_num = 50
    fields = ('text', 'ordering')


@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):
    inlines = [DuyuruTextInline, DuyuruImageInline]


class ImageTextInline(admin.TabularInline):
    model = Image
    extra = 1
    min = 0
    max_num = 200
    fields = ('image',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageTextInline]
