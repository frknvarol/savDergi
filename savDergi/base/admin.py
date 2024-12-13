from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Duyuru, Album, AlbumImage, DuyuruImage, DuyuruText, Sayi, MakaleYazar, \
    MakaleAnahtar, MakaleKaynak, Makale, Portre, Konferans, KonferansImage, Metodoloji, MetodolojiImage, \
    Sava, SavaImage

admin.site.register(Portre)


class DuyuruImageInline(admin.TabularInline):
    model = DuyuruImage
    extra = 1
    min = 0
    max_num = 50
    fields = ('image', 'ordering')


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
    model = AlbumImage
    extra = 1
    min = 0
    max_num = 200
    fields = ('image',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageTextInline]


class MakaleAnahtarInline(NestedStackedInline):
    model = MakaleAnahtar
    extra = 1
    min = 1
    max_num = 50
    fields = ('baslik', 'anahtar')


class MakaleKaynakInline(NestedStackedInline):
    model = MakaleKaynak
    extra = 1
    min = 1
    max_num = 50
    fields = ('baslik', 'kaynak')


class MakaleYazarInline(NestedStackedInline):
    model = MakaleYazar
    extra = 1
    min = 1
    max_num = 10
    fields = ('yazar',)


@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ('sayi', 'baslik', 'Oz', 'bolum', 'birinci_dil', 'created', 'pdf')


class MakaleInline(NestedStackedInline):
    model = Makale
    extra = 0
    min = 1
    max_num = 50
    inlines = [MakaleKaynakInline, MakaleAnahtarInline, MakaleYazarInline]


class SayiAdmin(NestedModelAdmin):
    list_display = ('sayi', 'created')
    inlines = [MakaleInline]


admin.site.register(Sayi, SayiAdmin)


class KonferansImageInline(admin.StackedInline):
    model = KonferansImage
    extra = 0
    min = 1
    max_num = 50


@admin.register(Konferans)
class MetodolojiAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'text')
    inlines = [KonferansImageInline]


class MetodolojiImageInline(admin.StackedInline):
    model = MetodolojiImage
    extra = 0
    min = 1
    max_num = 50


@admin.register(Metodoloji)
class MetodolojiAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'text')
    inlines = [MetodolojiImageInline]


class SavaImageInline(admin.StackedInline):
    model = SavaImage
    extra = 0
    min = 1
    max_num = 50


@admin.register(Sava)
class SavaAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'text')
    inlines = [SavaImageInline]

