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
    path('konferanslar', views.konferanslar, name='konferanslar'),
    path('konferanslar/<slug:slug>', views.konferans, name='konferans'),
    path('stajyer-avukatlık-atolyesi', views.sava, name='sava'),
    path('stajyer-avukatlık-atolyesi/<slug:slug>', views.sava_instance, name='sava_instance'),
    path('biz-kimiz', views.biz_kimiz, name='biz_kimiz'),
    path('bir-hukukcunun-portresi', views.hukukcu_portre, name='hukukcu_portre'),
    path('bir-hukukcunun-portresi/<slug:slug>', views.hukukcu_portre_instance, name='hukukcu_portre_instance'),
    path('metodoloji-egitimleri', views.metodoloji, name='metodoloji'),
    path('metodoloji-egitimleri/<slug:slug>', views.metodoloji_instance, name='metodoloji_instance'),
    path('duyurular', views.duyurular, name='duyurular'),
    path('duyurular/<slug:slug>/', views.duyuru, name='duyuru'),
    path('galeri', views.galeri, name='galeri'),
    path('galeri/<slug:slug>/', views.album, name='album'),
    path('dergi', views.dergi, name='dergi'),
    path('dergi/<slug:slug>/', views.sayi, name='sayi'),
    path('dergi/<slug:sayi_slug>/<slug:makale_slug>/', views.makale, name='makale'),
    path('pdf/<int:pk>/', views.view_pdf, name='view_pdf')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
