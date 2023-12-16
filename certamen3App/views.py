import os
from django.shortcuts import redirect, render
from certamen3App.models import Auto
from certamen3App.models import Marca
from certamen3App.forms import FormAuto
from certamen3App.forms import FormMarca
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'certamen3App/index.html')
@login_required
def listadoAutos(request):
    autos = Auto.objects.all()
    data = {'autos': autos}
    return render(request, 'certamen3App/autos.html', data)
@login_required
def agregarAuto(request):
    form = FormAuto()
    if request.method == 'POST' :
        form = FormAuto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'certamen3App/agregarAuto.html', data)
@login_required
def listadoMarcas(request):
    marcas = Marca.objects.all()
    data = {'marcas': marcas}
    return render(request, 'certamen3App/marcas.html', data)
@login_required
def agregarMarca(request):
    form = FormMarca()
    if request.method == 'POST' :
        form = FormMarca(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'certamen3App/agregarMarca.html', data)
@login_required
def eliminarMarca(request, nombre):
    marca = Marca.objects.get(nombre = nombre)
    marca.delete()
    return redirect('/marcas')
@login_required
def actualizarMarca(request, nombre):
    marca = Marca.objects.get(nombre = nombre)
    form = FormMarca(instance=marca)
    if request.method == 'POST':
        form = FormMarca(request.POST, instance=marca)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'certamen3App/agregarMarca.html', data)
@login_required
def eliminarAuto(request, id):
    auto = Auto.objects.get(id = id)
    print(auto.image)
    os.remove(str(f"media/{auto.image}"))
    auto.delete()
    return redirect('/autos')
@login_required
def actualizarAuto(request, id):
    auto = Auto.objects.get(id = id)
    form = FormAuto(instance=auto)
    if request.method == 'POST':
        form = FormAuto(request.POST, instance=auto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'certamen3App/agregarAuto.html', data)
