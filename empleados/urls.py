from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.empleadoHome, name='empleado_home'),
    path('create/', views.empleadoCreate, name='empleado_create'),
    path('edit/<int:personas_id>/', views.empleadoEdit, name='edit_empleado'),
    path('delete/<int:empleado_id>/', views.empleadoDelete, name='delete_empleado'),
]