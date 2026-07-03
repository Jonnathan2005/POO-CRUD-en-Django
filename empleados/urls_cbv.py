from django.urls import path
from . import views_cbv as views

urlpatterns = [
    path('cargos/', views.CargoListView.as_view(), name='cargo_list_cbv'),
    path('cargos/crear/', views.CargoCreateView.as_view(), name='cargo_create_cbv'),
    path('cargos/<int:pk>/editar/', views.CargoUpdateView.as_view(), name='cargo_update_cbv'),
    path('cargos/<int:pk>/eliminar/', views.CargoDeleteView.as_view(), name='cargo_delete_cbv'),

    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list_cbv'),
    path('empleados/crear/', views.EmpleadoCreateView.as_view(), name='empleado_create_cbv'),
    path('empleados/<int:pk>/editar/', views.EmpleadoUpdateView.as_view(), name='empleado_update_cbv'),
    path('empleados/<int:pk>/eliminar/', views.EmpleadoDeleteView.as_view(), name='empleado_delete_cbv'),
]