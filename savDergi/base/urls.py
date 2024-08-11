from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('amaç-ve-kapsam', views.amac_kapsam, name='amac_kapsam'),
    path('misyonumuz', views.misyonumuz, name='misyonumuz'),
    path('etik-ilkeler-ve-yayım-politikası', views.etik_ilkeler, name='etik_ilkeler'),
    path('yazım-kuralları', views.yazim_kurallari, name='yazim_kurallari'),
    path('dergi', views.dergi, name='dergi'),
    path('konferanslar', views.konferanslar, name='konferanslar'),
    path('stajyer-avukatlık-atolyesi', views.sava, name='sava'),
    path('biz-kimiz', views.biz_kimiz, name='biz_kimiz'),
    path('bir-hukukcunun-portresi', views.hukukcu_portre, name='hukukcu_portre'),
    path('metodoloji-egitimleri', views.metodoloji, name='metodoloji'),
    path('duyurular', views.duyurular, name='duyurular'),
    path('duyurular/<slug:slug>/', views.duyuru, name='duyuru'),
    path('galeri', views.galeri, name='galeri'),
    path('galeri/<str:album_name>/', views.album, name='album'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
