from django.contrib import admin
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText, Dergi, DergiYazar, \
    DergiAnahtar, DergiText, DergiKaynak

admin.site.register(EmbeddedVideo)
admin.site.register(Image)


@admin.register(DuyuruImage)
class DuyuruImageAdmin(admin.ModelAdmin):
    list_display = ('topic', 'image', 'created')


class DuyuruImageInline(admin.TabularInline):
    model = DuyuruImage
    extra = 1
    min = 0
    max_num = 50
    fields = ('image', 'ordering')


@admin.register(DuyuruText)
class DuyuruTextAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'created')


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


@admin.register(DergiAnahtar)
class DergiAnahtarAdmin(admin.ModelAdmin):
    list_display = ('topic', 'anahtar', 'created')


class DergiAnahtarInline(admin.TabularInline):
    model = DergiAnahtar
    extra = 1
    min = 1
    max_num = 50
    fields = ('topic', 'anahtar')


@admin.register(DergiKaynak)
class DergiKaynakAdmin(admin.ModelAdmin):
    list_display = ('topic', 'kaynak', 'created')


class DergiKaynakInline(admin.TabularInline):
    model = DergiKaynak
    extra = 1
    min = 1
    max_num = 50
    fields = ('topic', 'kaynak')


@admin.register(DergiText)
class DergiTextAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'created')


class DergiTextInline(admin.TabularInline):
    model = DergiText
    extra = 1
    min = 1
    max_num = 50
    fields = ('text', 'ordering')


@admin.register(DergiYazar)
class DergiYazarAdmin(admin.ModelAdmin):
    list_display = ('topic', 'yazar', 'created')


class DergiYazarInline(admin.TabularInline):
    model = DergiYazar
    extra = 1
    min = 1
    max_num = 10
    fields = ('yazar',)


@admin.register(Dergi)
class DergiAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created')
    inlines = [DergiTextInline, DergiKaynakInline, DergiAnahtarInline, DergiYazarInline]


