from django.urls import path
from . import views_fbv as views

urlpatterns = [
    path('cargos/', views.listar_cargos, name='cargo_list_fbv'),
    path('cargos/crear/', views.crear_cargo, name='cargo_create_fbv'),
    path('cargos/<int:cargo_id>/editar/', views.editar_cargo, name='cargo_update_fbv'),
    path('cargos/<int:cargo_id>/eliminar/', views.eliminar_cargo, name='cargo_delete_fbv'),

    path('empleados/', views.listar_empleados, name='empleado_list_fbv'),
    path('empleados/crear/', views.crear_empleado, name='empleado_create_fbv'),
    path('empleados/<int:empleado_id>/editar/', views.editar_empleado, name='empleado_update_fbv'),
    path('empleados/<int:empleado_id>/eliminar/', views.eliminar_empleado, name='empleado_delete_fbv'),
]