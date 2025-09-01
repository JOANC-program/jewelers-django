from django.contrib import admin
from django.urls import path
from django.urls import include
from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeClientes, name="clientes_home"),
    path('agregar/', views.agregarClientes, name="clientes_agregar"),
    path('eliminar/<int:clientes_id>/', views.eliminarClientes, name="clientes_eliminar"),
    path('editar/<int:clientes_id>/', views.editarClientes, name="clientes_editar"),
]