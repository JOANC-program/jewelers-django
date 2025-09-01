from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

def index(request):
    Productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': Productos})
def create(request):
    return render(request, 'create.html')
def edit(request):
    return render(request, 'edit.html')
