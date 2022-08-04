from turtle import ondrag
from django.db import models

# Create your models here
# Creacion de la clase Categoria
class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_cat

# Creacion de la clase Libro 
class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo_libro = models.CharField(max_length=200)
    autor_libro = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    # Se define ForeignKey porque un mismo autor escribe muchos libros
    sumario_libro = models.TextField(max_length=1000, help_text="Describa el libro")
    isbn_libro = models.CharField(max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    def __str__(self):
        return self.titulo_libro

# Creacion de la clase Autor
class Autor(models.Model):
    nombre_autor= models.CharField(max_length=100)
    apellido_autor=models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' %(self.apellido_autor, self.nombre_autor)

