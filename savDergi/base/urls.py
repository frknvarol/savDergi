from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('amaç-ve-kapsam', views.amac_kapsam, name='amac_kapsam'),
    path('misyonumuz', views.misyonumuz, name='misyonumuz'),
    path('etik-ilkeler-ve-yayım-politikası', views.etik_ilkeler, name='etik_ilkeler'),
    path('yazım-kuralları', views.yazim_kurallari, name='yazim_kurallari'),
]