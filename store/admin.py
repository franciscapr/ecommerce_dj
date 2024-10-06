from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')   # Campos que queremos listar en el admin
    prepopulated_fields = {'slug': ('product_name',)}    # Indicamos como autorrellenamos
    
    # Registramos la entidad
admin.site.register(Product, ProductAdmin)