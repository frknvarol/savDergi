from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText, Dergi, DergiMakale, DergiSource, \
    DergiKeyword, DergiMakaleText

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


@admin.register(DergiKeyword)
class DergiKeywordAdmin(admin.ModelAdmin):
    list_display = ('title', 'keyword', 'created')


class DergiKeywordInline(NestedTabularInline):
    model = DergiKeyword
    extra = 0
    min = 1
    max_num = 50
    fields = ('title', 'keyword', 'ordering')


@admin.register(DergiSource)
class DergiSourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'created')


class DergiSourceInline(NestedTabularInline):
    model = DergiSource
    extra = 0
    min = 1
    max_num = 50
    fields = ('title', 'source', 'ordering')


@admin.register(DergiMakaleText)
class DergiMakaleTextAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text', 'created')


class DergiMakaleTextInline(NestedTabularInline):
    model = DergiMakaleText
    extra = 0
    min = 1
    max_num = 50
    fields = ('text', 'ordering')


@admin.register(DergiMakale)
class DergiMakaleAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'created')


class DergiMakaleInline(NestedStackedInline):
    model = DergiMakale
    inlines = [DergiMakaleTextInline,]
    extra = 0
    min = 1
    max_num = 50
    fields = ('topic', 'author', 'ordering')


class DergiAdmin(NestedModelAdmin):
    model = Dergi
    inlines = [DergiMakaleInline, DergiKeywordInline, DergiSourceInline]


admin.site.register(Dergi, DergiAdmin)

