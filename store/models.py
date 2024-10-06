from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)    # Puede tener valores nulos
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    # Cuando se elimine la categoria, se realiza una proceso de cascada que tambien elimina los productos relacionados a esta categoria
    created_date = models.DateTimeField(auto_now_add=True)    # Se autogenera la fecha de creación
    modified_date = models.DateTimeField(auto_now=True)    # Fecha de modificación
    
    # Listamos los productos por una label especifico
    def __str__(self):
        return self.product_name