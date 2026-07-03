from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Cargo
class CargoListView(LoginRequiredMixin, ListView):
    model = Cargo
    template_name = 'empleados/cbv/cargo_list.html'
    context_object_name = 'cargos'

class CargoCreateView(LoginRequiredMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/cbv/cargo_form.html'
    success_url = reverse_lazy('cargo_list_cbv')

class CargoUpdateView(LoginRequiredMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/cbv/cargo_form.html'
    success_url = reverse_lazy('cargo_list_cbv')

class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo
    template_name = 'empleados/cbv/cargo_confirm_delete.html'
    success_url = reverse_lazy('cargo_list_cbv')


# Empleado

class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/cbv/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/cbv/empleado_form.html'
    success_url = reverse_lazy('empleado_list_cbv')

class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/cbv/empleado_form.html'
    success_url = reverse_lazy('empleado_list_cbv')

class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/cbv/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list_cbv')