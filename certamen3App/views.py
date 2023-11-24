from django.shortcuts import render
from certamen3App.models import Auto
from certamen3App.forms import FormAuto
# Create your views here.

def index(request):
    return render(request, 'certamen3App/index.html')

def listadoAutos(request):
    autos = Auto.objects.all()
    data = {'autos': autos}
    return render(request, 'certamen3App/autos.html', data)

def agregarAuto(request):
    form = FormAuto()
    if request.method == 'POST' :
        form = FormAuto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'certamen3App/agregarAuto.html', data)


# def eliminarProyecto(request, id):
#    proyecto = Proyecto.objects.get(id = id)