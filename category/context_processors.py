from .models import Category


# Creamos una función, recibe request
def menu_links(request):
    links = Category.objects.all()    # Obtenemos todas la categorias
    return dict(links=links)    # Nos retorna un diccionario con los valores de links