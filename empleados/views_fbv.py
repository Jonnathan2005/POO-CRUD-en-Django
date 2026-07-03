from django.shortcuts import render, redirect, get_object_or_404
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm
from django.contrib.auth.decorators import login_required


# Cargo
@login_required
def listar_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'empleados/fbv/cargo_list.html', {'cargos': cargos})

@login_required
def crear_cargo(request):
    if request.method == 'GET':
        return render(request, 'empleados/fbv/cargo_form.html', {'form': CargoForm})
    else:
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_list_fbv')
        return render(request, 'empleados/fbv/cargo_form.html', {
            'form': form,
            'error': 'Datos inválidos'
        })

@login_required
def editar_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    if request.method == 'GET':
        form = CargoForm(instance=cargo)
        return render(request, 'empleados/fbv/cargo_form.html', {'form': form})
    else:
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo_list_fbv')
        return render(request, 'empleados/fbv/cargo_form.html', {
            'form': form,
            'error': 'Datos inválidos'
        })

@login_required
def eliminar_cargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo_list_fbv')
    return render(request, 'empleados/fbv/cargo_confirm_delete.html', {'cargo': cargo})


# Empleado
@login_required
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/fbv/empleado_list.html', {'empleados': empleados})

@login_required
def crear_empleado(request):
    if request.method == 'GET':
        return render(request, 'empleados/fbv/empleado_form.html', {'form': EmpleadoForm})
    else:
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list_fbv')
        return render(request, 'empleados/fbv/empleado_form.html', {
            'form': form,
            'error': 'Datos inválidos'
        })

@login_required
def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'GET':
        form = EmpleadoForm(instance=empleado)
        return render(request, 'empleados/fbv/empleado_form.html', {'form': form})
    else:
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_list_fbv')
        return render(request, 'empleados/fbv/empleado_form.html', {
            'form': form,
            'error': 'Datos inválidos'
        })

@login_required
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_list_fbv')
    return render(request, 'empleados/fbv/empleado_confirm_delete.html', {'empleado': empleado})