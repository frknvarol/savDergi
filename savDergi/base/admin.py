from django.contrib import admin
from nested_inline.admin import NestedStackedInline
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText, Sayi, MakaleYazar, \
    MakaleAnahtar, MakaleText, MakaleKaynak, Makale

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


@admin.register(MakaleAnahtar)
class MakaleAnahtarAdmin(admin.ModelAdmin):
    list_display = ('konu', 'anahtar', 'created')


class MakaleAnahtarInline(NestedStackedInline):
    model = MakaleAnahtar
    extra = 1
    min = 1
    max_num = 50
    fields = ('konu', 'anahtar')


@admin.register(MakaleKaynak)
class MakaleKaynakAdmin(admin.ModelAdmin):
    list_display = ('konu', 'kaynak', 'created')


class MakaleKaynakInline(NestedStackedInline):
    model = MakaleKaynak
    extra = 1
    min = 1
    max_num = 50
    fields = ('konu', 'kaynak')


@admin.register(MakaleText)
class MakaleTextAdmin(admin.ModelAdmin):
    list_display = ('konu', 'text', 'created')


class MakaleTextInline(NestedStackedInline):
    model = MakaleText
    extra = 1
    min = 1
    max_num = 50
    fields = ('text', 'ordering')


@admin.register(MakaleYazar)
class MakaleYazarAdmin(admin.ModelAdmin):
    list_display = ('konu', 'yazar', 'created')


class MakaleYazarInline(NestedStackedInline):
    model = MakaleYazar
    extra = 1
    min = 1
    max_num = 10
    fields = ('yazar',)


@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ('sayi', 'konu', 'Oz', 'bolum', 'birinci_dil', 'created', 'pdf')


class MakaleInline(NestedStackedInline):
    model = Makale
    extra = 0
    min = 1
    max_num = 50
    inlines = [MakaleTextInline, MakaleKaynakInline, MakaleAnahtarInline, MakaleYazarInline]


@admin.register(Sayi)
class SayiAdmin(admin.ModelAdmin):
    list_display = ('sayi', 'created')
    inlines = [MakaleInline]


