from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


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


def dergi(request):
    context = {'page_css': 'savDergi/css/dergi.css'}
    return render(request, 'base/dergi.html', context)


def galeri(request):
    context = {'page_css': 'savDergi/css/galeri.css'}
    return render(request, 'base/galeri.html', context)


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


def duyuru(request):
    context = {'page_css': 'savDergi/css/duyuru.css'}
    return render(request, 'base/duyuru.html', context)
