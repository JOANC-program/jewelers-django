from django.shortcuts import render, redirect
from .models import Cliente
from .form import ClienteForm

def homeClientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes':clientes}
    return render(request, 'homeCli.html', context)

def agregarClientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_home')
    else:
        form = ClienteForm()
    context = {'form':form}
    return render(request, 'agregarCli.html', context)

def eliminarClientes(request, clientes_id):
    clientes = Cliente.objects.get(id=clientes_id)
    clientes.delete()
    return redirect("clientes_home")

def editarClientes(request, clientes_id):
    clientes = Cliente.objects.get(id=clientes_id)
    if request.method=="POST":
        form=ClienteForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect("clientes_home")
    else:
        form = ClienteForm(intance=clientes)
    context={"form":form}
    return render(request, "editarCli.html", context)
    
# Create your views here.
