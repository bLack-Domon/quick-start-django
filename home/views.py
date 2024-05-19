from django.shortcuts import render

def Beranda(request):
    return render(request, 'beranda.html')
