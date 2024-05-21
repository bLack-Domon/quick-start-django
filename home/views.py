from django.shortcuts import render

def Beranda(request):
    return render(request, 'beranda.html')

def Kontak(request):
    return render(request, 'kontak.html')