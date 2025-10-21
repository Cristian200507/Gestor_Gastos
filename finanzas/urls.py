from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_gasto/', views.agregar_gasto, name='agregar_gasto'),
    path('agregar_ingreso/', views.agregar_ingreso, name='agregar_ingreso'),
    path('editar_gasto/<int:id>/', views.editar_gasto, name='editar_gasto'),
    path('editar_ingreso/<int:id>/', views.editar_ingreso, name='editar_ingreso'),
    path('eliminar_gasto/<int:id>/', views.eliminar_gasto, name='eliminar_gasto'),
    path('eliminar_ingreso/<int:id>/', views.eliminar_ingreso, name='eliminar_ingreso'),
    path('detalle_gasto/<int:id>/', views.detalle_gasto, name='detalle_gasto'),
    path('detalle_ingreso/<int:id>/', views.detalle_ingreso, name='detalle_ingreso'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),

]
