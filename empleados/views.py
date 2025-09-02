from django.shortcuts import render, redirect
from .models import Empleado
from .form import EmpleadoForm
# Create your views here.

def empleadoHome(request):
    empleados=Empleado.objects.all()
    context={'empleados':empleados}
    return render(request, 'home.html', context)

def empleadoCreate(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_home')
    else:
        form = EmpleadoForm
    context = {'form': form}
    return render(request, 'create.html', context)

def empleadoDelete(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.delete()
    return redirect("empleado_home")

def empleadoEdit(request, personas_id):
    empleado = Empleado.objects.get(id=personas_id)
    if request.method == "POST":
        form=EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect("empleado_home")
    else:
        form=EmpleadoForm(instance=empleado)
    context={"form":form}
    return render(request, "edit.html", context)