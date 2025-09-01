from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/create/', views.create, name='create'),
    path('productos/edit/', views.edit, name='edit'),
]