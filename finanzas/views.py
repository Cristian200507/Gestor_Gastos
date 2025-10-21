from django.shortcuts import render, redirect, get_object_or_404
from .models import Gasto, Ingreso
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .forms import GastoForm, IngresoForm
import json


@login_required
def inicio(request):
    gastos = Gasto.objects.filter(usuario=request.user)
    ingresos = Ingreso.objects.filter(usuario=request.user)

    total_gastos = sum(g.monto for g in gastos)
    total_ingresos = sum(i.monto for i in ingresos)
    balance = total_ingresos - total_gastos

    return render(request, 'finanzas/inicio.html', {
        'gastos': gastos,
        'ingresos': ingresos,
        'total_gastos': total_gastos,
        'total_ingresos': total_ingresos,
        'balance': balance,
    })


@login_required
def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            messages.success(request, 'Gasto agregado correctamente.')
            return redirect('inicio')
    else:
        form = GastoForm()
    return render(request, 'finanzas/agregar_gasto.html', {'form': form})


@login_required
def agregar_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.usuario = request.user
            ingreso.save()
            messages.success(request, 'Ingreso agregado correctamente.')
            return redirect('inicio')
    else:
        form = IngresoForm()
    return render(request, 'finanzas/agregar_ingreso.html', {'form': form})


@login_required
def editar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id, usuario=request.user)

    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gasto actualizado correctamente.')
            return redirect('inicio')
    else:
        form = GastoForm(instance=gasto)

    return render(request, 'finanzas/editar_gasto.html', {'form': form})


@login_required
def editar_ingreso(request, id):
    ingreso = get_object_or_404(Ingreso, id=id, usuario=request.user)

    if request.method == 'POST':
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingreso actualizado correctamente.')
            return redirect('inicio')
    else:
        form = IngresoForm(instance=ingreso)

    return render(request, 'finanzas/editar_ingreso.html', {'form': form})


@login_required
def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id, usuario=request.user)
    gasto.delete()
    messages.info(request, 'Gasto eliminado correctamente.')
    return redirect('inicio')


@login_required
def eliminar_ingreso(request, id):
    ingreso = get_object_or_404(Ingreso, id=id, usuario=request.user)
    ingreso.delete()
    messages.info(request, 'Ingreso eliminado correctamente.')
    return redirect('inicio')


@login_required
def detalle_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id, usuario=request.user)
    return render(request, 'finanzas/detalle_gasto.html', {'gasto': gasto})


@login_required
def detalle_ingreso(request, id):
    ingreso = get_object_or_404(Ingreso, id=id, usuario=request.user)
    return render(request, 'finanzas/detalle_ingreso.html', {'ingreso': ingreso})


@login_required
def estadisticas(request):
    gastos_por_categoria = (
        Gasto.objects
        .filter(usuario=request.user)
        .values('categoria')
        .annotate(total=Sum('monto'))
        .order_by('categoria')
    )

    ingresos_por_categoria = (
        Ingreso.objects
        .filter(usuario=request.user)
        .values('categoria')
        .annotate(total=Sum('monto'))
        .order_by('categoria')
    )

    gastos_dict = {item['categoria']: float(item['total']) for item in gastos_por_categoria}
    ingresos_dict = {item['categoria']: float(item['total']) for item in ingresos_por_categoria}

    context = {
    'gastos_por_categoria': json.dumps(gastos_dict),
    'ingresos_por_categoria': json.dumps(ingresos_dict),
}

    return render(request, 'finanzas/estadisticas.html', context)
