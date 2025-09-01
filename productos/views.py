from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import redirect

def index(request):
    Productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': Productos})
def create(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'create.html', {'form': form})
def edit(request,id):
    producto = Producto.objects.get (id=id)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('index')
    return render(request, 'edit.html', {'form': form})
def delete(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('index')
