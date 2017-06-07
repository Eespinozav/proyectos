from django import forms

from Apps.Home.models import Formulario

class ContactoForms(forms.ModelForm):

    class Meta:
        model = Formulario

        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'comentario',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apallido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'E-Mail',
            'comentario': 'Comentario',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control'}),
        }