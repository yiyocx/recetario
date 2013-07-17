from principal.models import Bebida
from principal.models import Receta
from django.shortcuts import render_to_response

def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	return render_to_response('lista_bebidas.html',{'lista':bebidas})

def lista_recetas(request):
	recetas = Receta.objects.all()
	return render_to_response('lista_bebidas.html',{'lista_recetas':recetas})