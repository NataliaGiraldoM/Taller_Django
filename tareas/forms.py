from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completado']

    # Validación del título
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')

        if not titulo:
            raise forms.ValidationError("El título es obligatorio")

        if len(titulo) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres")

        return titulo

    # Validación de la descripción
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')

        if not descripcion:
            raise forms.ValidationError("La descripción es obligatoria")

        if len(descripcion) < 5:
            raise forms.ValidationError("La descripción debe ser más detallada")

        return descripcion
