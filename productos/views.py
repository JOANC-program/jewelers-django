from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def create(request):
    return render(request, 'create.html')
def edit(request):
    return render(request, 'edit.html')
