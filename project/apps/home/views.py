from django.shortcuts import render, redirect

from .import forms
# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def crear_usuario(request):
    if request.method == 'POST':
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.UsuarioForm()
        context = {"form": form}
        return render(request, "home/crear_usuario.html", context)
    
def crear_organizacion(request):
    if request.method == 'POST':
        form = forms.OrganizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = forms.OrganizacionForm()
        context = {"form": form}
        return render(request, "home/crear_organizacion.html", context)