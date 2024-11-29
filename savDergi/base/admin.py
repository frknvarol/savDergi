from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText, Dergi, DergiMakale,  \
    DergiMakaleYazar, DergiMakaleAnahtar, DergiMakaleText, DergiMakaleKaynak

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


@admin.register(DergiMakaleAnahtar)
class DergiMakaleAnahtarAdmin(admin.ModelAdmin):
    list_display = ('topic', 'anahtar', 'created')


class DergiMakaleAnahtarInline(NestedTabularInline):
    model = DergiMakaleAnahtar
    extra = 0
    min = 1
    max_num = 50
    fields = ('topic', 'anahtar', 'ordering')


@admin.register(DergiMakaleKaynak)
class DergiMakaleKaynakAdmin(admin.ModelAdmin):
    list_display = ('topic', 'kaynak', 'created')


class DergiMakaleKaynakInline(NestedTabularInline):
    model = DergiMakaleKaynak
    extra = 0
    min = 1
    max_num = 50
    fields = ('topic', 'kaynak', 'ordering')


@admin.register(DergiMakaleText)
class DergiMakaleTextAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'created')


class DergiMakaleTextInline(NestedTabularInline):
    model = DergiMakaleText
    extra = 0
    min = 1
    max_num = 50
    fields = ('text', 'ordering')


@admin.register(DergiMakaleYazar)
class DergiMakaleYazarAdmin(admin.ModelAdmin):
    list_display = ('yazar', 'created')


class DergiMakaleYazarInline(NestedTabularInline):
    model = DergiMakaleYazar
    extra = 1
    min = 1
    max_num = 10
    fields = ('yazar',)


@admin.register(DergiMakale)
class DergiMakaleAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created')


class DergiMakaleInline(NestedStackedInline):
    model = DergiMakale
    inlines = [DergiMakaleTextInline, DergiMakaleKaynakInline, DergiMakaleAnahtarInline, DergiMakaleYazarInline]
    extra = 0
    min = 1
    max_num = 50
    fields = ('topic', 'ordering', 'konu', 'Oz', 'bolum', 'pdf')


class DergiAdmin(NestedModelAdmin):
    model = Dergi
    inlines = [DergiMakaleInline,]


admin.site.register(Dergi, DergiAdmin)

