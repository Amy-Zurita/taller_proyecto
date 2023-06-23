from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from citasmd.forms import CitasMdFormulario
from citasmd.models import CitasMd


# Create your views here.


def agregar_citasmd(request):
    pagina = loader.get_template('agregar_citasmd.html')
    if request.method == 'GET':
        formulario= CitasMdFormulario
    elif request.method == 'POST':
        formulario= CitasMdFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_citasmd(request, idCitasMd):
    pagina= loader.get_template('ver_citasmd.html')
    citasmd= get_object_or_404(CitasMd, pk=idCitasMd)
    mensaje= {'citasmd': citasmd}
    return HttpResponse(pagina.render(mensaje, request))


def editar_citasmd(request, idCitasMd):
    pagina= loader.get_template('editar_citasmd.html')
    citasmd= get_object_or_404(CitasMd, pk=idCitasMd)
    if request.method == 'GET':
        formulario= CitasMdFormulario(instance=citasmd)
    elif request.method == 'POST':
        formulario= CitasMdFormulario(request.POST, instance=citasmd)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    mensaje= {'formulario': formulario}
    return HttpResponse(pagina.render(mensaje,request))

def eliminar_citasmd(request, idCitasMd):
    citasmd = get_object_or_404(CitasMd, pk=idCitasMd)
    if citasmd:
        citasmd.delete()
        return redirect('inicio')
