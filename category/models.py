from django.db import models

# Create your models here.
# Creamos una clase que represente la categoria

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True) # Valor unico
    description = models.CharField(max_length=255, blank=True) # Permite valores nulos
    slug = models.CharField(max_length=100, unique=True) # Valor unico
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) # Permite nulos
    
    # Para ver la data de forma representativa utilizamos el str
    def __str__(self):
        return self.category_name    # Lo que queremos que se nos muestre en la estructura de nuestro models es el cateogry_name