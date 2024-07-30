from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('amaç-ve-kapsam', views.amac_kapsam, name='amac_kapsam'),
    path('misyonumuz', views.misyonumuz, name='misyonumuz'),
    path('etik-ilkeler-ve-yayım-politikası', views.etik_ilkeler, name='etik_ilkeler'),
    path('yazım-kuralları', views.yazim_kurallari, name='yazim_kurallari'),
    path('dergi', views.dergi, name='dergi'),
    path('galeri', views.galeri, name='galeri'),
    path('konferanslar', views.konferanslar, name='konferanslar'),
    path('stajyer-avukatlık-atolyesi', views.sava, name='sava'),
]
