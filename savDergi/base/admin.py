from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText, Dergi, DergiSayi, DergiSayiYazar, \
    DergiSayiAnahtar, DergiSayiText, DergiSayiKaynak

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


@admin.register(DergiSayiAnahtar)
class DergiSayiAnahtarAdmin(admin.ModelAdmin):
    list_display = ('topic', 'anahtar', 'created')


class DergiSayiAnahtarInline(NestedTabularInline):
    model = DergiSayiAnahtar
    extra = 0
    min = 1
    max_num = 50
    fields = ('topic', 'anahtar', 'ordering')


@admin.register(DergiSayiKaynak)
class DergiSayiKaynakAdmin(admin.ModelAdmin):
    list_display = ('topic', 'kaynak', 'created')


class DergiSayiKaynakInline(NestedTabularInline):
    model = DergiSayiKaynak
    extra = 0
    min = 1
    max_num = 50
    fields = ('topic', 'kaynak', 'ordering')


@admin.register(DergiSayiText)
class DergiSayiTextAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'created')


class DergiSayiTextInline(NestedTabularInline):
    model = DergiSayiText
    extra = 0
    min = 1
    max_num = 50
    fields = ('text', 'ordering')


@admin.register(DergiSayiYazar)
class DergiSayiYazarAdmin(admin.ModelAdmin):
    list_display = ('yazar', 'created')


class DergiSayiYazarInline(NestedTabularInline):
    model = DergiSayiYazar
    extra = 1
    min = 1
    max_num = 10
    fields = ('yazar',)


@admin.register(DergiSayi)
class DergiSayiAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created')


class DergiSayiInline(NestedStackedInline):
    model = DergiSayi
    inlines = [DergiSayiTextInline, DergiSayiKaynakInline, DergiSayiAnahtarInline, DergiSayiYazarInline]
    extra = 0
    min = 1
    max_num = 50
    fields = ('topic', 'konu', 'Oz', 'bolum', 'birinci_dil', 'pdf', 'ordering')


class DergiAdmin(NestedModelAdmin):
    model = Dergi
    inlines = [DergiSayiInline,]


admin.site.register(Dergi, DergiAdmin)

