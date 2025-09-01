from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('productos/edit/<int:id>/', views.edit, name='edit'),
]