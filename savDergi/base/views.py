from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def amac_kapsam(request):
    return render(request, 'base/amac_kapsam.html')
