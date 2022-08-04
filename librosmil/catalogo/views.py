from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Crea la vista index 
def index(request):
    return HttpResponse("Bienvenido al Catalogo de Libros")

