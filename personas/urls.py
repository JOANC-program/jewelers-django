from django.contrib import admin
from django.urls import path
from django.urls import include
from personas import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.homePersonas, name="personas_home" ),
    path("agregar/", views.agregarPersonas, name="personas_agregar"),
    path("eliminar/<int:personas_id>/", views.eliminarPersonas, name="personas_eliminar"),
    path("editar/<int:personas_id>/", views.editarPersonas, name="personas_editar"),

]