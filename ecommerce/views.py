from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)    # Solicitamos todos los productos
    
    context = {
        'products': products,    # Definimos los prodcutos en un diccionario
    }
    
    
    return render(request, 'home.html', context)    # Pasamos el diccionario al render para poder usarlos en el home