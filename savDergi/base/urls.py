from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('amac_kapsam', views.amac_kapsam, name='amac_kapsam')
]
