from django.shortcuts import render

# Create your views here.

def homeEmpleado(request):
    return render(request, 'home.html')
def createEmpleado(request):
    return render(request, 'create.html')
def editEmpleado(request):
    return render(request, 'edit.html')