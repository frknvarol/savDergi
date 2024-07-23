from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def amac_kapsam(request):
    return render(request, 'base/amac_kapsam.html')


def misyonumuz(request):
    return render(request, 'base/misyonumuz.html')


def etik_ilkeler(request):
    return render(request, 'base/etik_ilkeler_ve_yayım_politikası.html')


def yazim_kurallari(request):
    return render(request, 'base/yazım_kuralları.html')

