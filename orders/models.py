from django.db import models
from accounts.models import Account
from store.models import Product, Variation

# Create your models here.
# Crearemos tres tablas

class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)    # Tenemos una referencia entre la tablas usuarios Accoun con la tabla peyment, si eleiminamos el usuario tmb se debe eliminar el record de payment
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    crrated_at = models.DateTimeField(auto_now_add=True)    # Se autogenere el valor actual
    
    def __str__(self):
        return self.payment_id
    
# Creamos la tabla de orden de compra
class Order(models.Model):
    STATUS = (
        ('New', 'Nuevo'),
        ('Accepted', 'Aceptado'),
        ('Complete', 'Completado'),
        ('Cancelled', 'Cancelado'),
    )
    
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    addres_line_1 = models.CharField(max_length=100)
    addres_line_2 = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    order_note = models.CharField(max_length=100, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Creamos la función que represente los records de esta tabla orders dentro de admin
    def __str__(self):
        return self.user.first_name
    
# Creamos la tabla Order Product
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)    # Relacionamos con la tabla Order
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
