from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.Home.forms import ContactoForms

# Create your views here.
def index(request):
    return render(request, 'Home/index.html')

def contacto_view(request):
    form = ContactoForms()
    if request.method == 'POST':
        form = ContactoForms(request.POST)
        print( form)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj.nombre)
            form.save()
        return redirect('home:contacto_enviar')

    return render(request, 'Home/contacto_form.html', {'form':form})

def administracion(request):
    return render(request, 'Home/administracion.html')

def quienes_somos(request):
    return render(request, 'Home/quienes_somos.html')

def informatica(request):
    return render(request, 'Home/informatica.html')

def servprofesionales(request):
    return render(request, 'Home/servprofesionales.html')