from django.contrib import admin
from .models import Categoria, Libro, Autor
# Register your models here.
# Se registran los modelos creados.
admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(Autor) 