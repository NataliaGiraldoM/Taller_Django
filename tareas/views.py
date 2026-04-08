from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm


# READ
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista.html', {'tareas': tareas})


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
