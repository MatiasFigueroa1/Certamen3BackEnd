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

from .serializers import AutoSerializer
from .serializers import MarcaSerializer
from . import forms
from .models import Marca
from .models import Auto

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def autos_list(request):
    if request.method=='GET':
        autos=Auto.objects.all()#.order_by("fecha")
        ser=AutoSerializer(autos, many=True)
        return Response(ser.data)
    if request.method=='POST':
        ser=AutoSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def autos_detail(request, pk):
    try:
        auto=Auto.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        ser=AutoSerializer(auto)
        return Response(ser.data)
    if request.method == 'PUT':
        ser=AutoSerializer(auto, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        auto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def marcas_list(request):
    if request.method=='GET':
        marcas=Marca.objects.all()#.order_by("fecha")
        ser=MarcaSerializer(marcas, many=True)
        return Response(ser.data)
    if request.method=='POST':
        ser=MarcaSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def marcas_detail(request, pk):
    try:
        marca=Marca.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        ser=MarcaSerializer(marca)
        return Response(ser.data)
    if request.method == 'PUT':
        ser=MarcaSerializer(marca, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        marca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
