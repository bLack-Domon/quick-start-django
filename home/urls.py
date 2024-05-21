from django.urls import path
from . import views

urlpatterns = [
    path('', views.Beranda, name='index'),
    path('', views.Kontak, name='contact'),
]
