from django.shortcuts import render

def comienzo(request):
    return render(request,"comienzo/index.html")

def template1(request):
     return render(request,"template1.html")

def acerca_de_mi(request):
    return render(request,"comienzo/acerca_de_mi.html")