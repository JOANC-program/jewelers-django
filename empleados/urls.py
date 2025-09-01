from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeEmpleado, name='homeEmpleado'),
    path('empleados/create/', views.createEmpleado, name='createEmpleado'),
    path('empleados/edit/', views.editEmpleado, name='editEmpleado'),
]