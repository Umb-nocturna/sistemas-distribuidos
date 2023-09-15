from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"pages/inicio1.html",{})


def proyectos(request):
    return render(request,"pages/proyectos.html",{})