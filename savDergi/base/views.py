from django.shortcuts import render
from itertools import chain
from operator import attrgetter
from .models import Duyuru, Album, Image, EmbeddedVideo, DuyuruImage, DuyuruText, Sayi, Makale, \
    MakaleAnahtar, MakaleText, MakaleKaynak, MakaleYazar


def home(request):
    duyurus = Duyuru.objects.all()[:2]
    videos = EmbeddedVideo.objects.all()

    context = {'duyurus': duyurus, 'videos': videos}
    return render(request, 'base/home.html', context)


def amac_kapsam(request):
    context = {'page_css': 'savDergi/css/amac_kapsam.css'}
    return render(request, 'base/amac_kapsam.html', context)


def misyonumuz(request):
    context = {'page_css': 'savDergi/css/misyonumuz.css'}
    return render(request, 'base/misyonumuz.html', context)


def etik_ilkeler(request):
    context = {'page_css': 'savDergi/css/etik_ilkeler_ve_yayım_politikası.css'}
    return render(request, 'base/etik_ilkeler_ve_yayım_politikası.html', context)


def yazim_kurallari(request):
    context = {'page_css': 'savDergi/css/yazım_kuralları.css'}
    return render(request, 'base/yazım_kuralları.html', context)


def konferanslar(request):
    context = {'page_css': 'savDergi/css/konferanslar.css'}
    return render(request, 'base/konferanslar.html', context)


def sava(request):
    context = {'page_css': 'savDergi/css/sava.css'}
    return render(request, 'base/sava.html', context)


def biz_kimiz(request):
    context = {'page_css': 'savDergi/css/biz_kimiz.css'}
    return render(request, 'base/biz_kimiz.html', context)


def metodoloji(request):
    context = {'page_css': 'savDergi/css/metodoloji.css'}
    return render(request, 'base/metodoloji.html', context)


def hukukcu_portre(request):
    context = {'page_css': 'savDergi/css/hukukcu_portre.css'}
    return render(request, 'base/hukukcu_portre.html', context)


def duyurular(request):
    duyuru_group = Duyuru.objects.all()

    first_duyuru = []

    for duyuru in duyuru_group:
        first_text = sorted(DuyuruText.objects.filter(topic=duyuru), key=attrgetter('ordering'))[0]
        first_duyuru.append((duyuru, first_text))

    context = {'page_css': 'savDergi/css/duyurular.css', 'duyuru_group': first_duyuru}
    return render(request, 'base/duyurular.html', context)


def duyuru(request, slug):
    duyuru = Duyuru.objects.get(slug=slug)

    texts = DuyuruText.objects.filter(topic=duyuru)
    images = DuyuruImage.objects.filter(topic=duyuru)

    duyurular = (*sorted(chain(texts, images), key=attrgetter('ordering')),)

    context = {'duyuru': duyuru, 'duyurular': duyurular, 'page_css': 'savDergi/css/duyuru.css'}
    return render(request, 'base/duyuru.html', context)


def galeri(request):
    albums = Album.objects.all()
    album_images = []

    for album in albums:
        first_image = Image.objects.filter(name=album).first()
        album_images.append((album, first_image))
    context = {'page_css': 'savDergi/css/galeri.css', 'album_images': album_images}
    return render(request, 'base/galeri.html', context)


def album(request, slug):
    album = Album.objects.get(slug=slug)
    images = Image.objects.filter(name=album)
    context = {'images': images, 'slug': slug, 'page_css': 'savDergi/css/galeri.css'}
    return render(request, 'base/album.html', context)


def dergi(request):
    sayi_group = Sayi.objects.all()

    context = {'page_css': 'savDergi/css/dergi.css', 'sayi_group': sayi_group}
    return render(request, 'base/dergi.html', context)


def sayi(request, slug):
    sayi = Sayi.objects.get(slug=slug)
    makaleler = Makale.objects.filter(sayi=sayi)
    kaynaklar = MakaleKaynak.objects.filter(konu__in=makaleler)
    anahtarlar = MakaleAnahtar.objects.filter(konu__in=makaleler)
    yazarlar = MakaleYazar.objects.filter(konu__in=makaleler)

    context = {'sayi': sayi, 'makaleler': makaleler, 'kaynaklar': kaynaklar, 'anahtarlar': anahtarlar, 'yazarlar': yazarlar, 'page_css': 'savDergi/css/sayi.css'}

    return render(request, 'base/sayi.html', context)


