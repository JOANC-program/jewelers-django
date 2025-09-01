from django.shortcuts import render, redirect
from .models import Persona
from .form import PersonaForm

def homePersonas(request):
    personas=Persona.objects.all()
    context={'personas':personas}
    return render(request, 'home.html', context)

def agregarPersonas(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personas_home')
    else:
        form = PersonaForm
    context = {'form': form}
    return render(request, 'agregar.html', context)

def eliminarPersonas(request, personas_id):
    persona = Persona.objects.get(id=personas_id)
    persona.delete()
    return redirect("personas_home")

def editarPersonas(request, personas_id):
    persona = Persona.objects.get(id=personas_id)
    if request.method == "POST":
        form=PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect("personas_home")
    else:
        form=PersonaForm(instance=persona)
    context={"form":form}
    return render(request, "editar.html", context)