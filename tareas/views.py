from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tarea
from .forms import TareaForm

# READ - solo pendientes
def lista_tareas(request):
    fecha = request.GET.get('fecha')
    tareas = Tarea.objects.filter(completado=False)
    if fecha:
        tareas = tareas.filter(fecha=fecha)
    return render(request, 'lista.html', {'tareas': tareas, 'fecha_filtro': fecha})

# COMPLETADAS
def tareas_completadas(request):
    tareas = Tarea.objects.filter(completado=True)
    return render(request, 'completadas.html', {'tareas': tareas})

# CREATE
def crear_tarea(request):
    form = TareaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Tarea creada correctamente")
        return redirect('lista')
    return render(request, 'form.html', {'form': form})

# UPDATE
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    form = TareaForm(request.POST or None, instance=tarea)
    if form.is_valid():
        form.save()
        messages.success(request, "Tarea actualizada correctamente")
        return redirect('lista')
    return render(request, 'form.html', {'form': form})

# DELETE
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, "Tarea eliminada correctamente")
        return redirect('lista')
    return render(request, 'eliminar.html', {'tarea': tarea})

# TOGGLE COMPLETADO
def completar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.completado = not tarea.completado
    tarea.save()
    return redirect('lista')