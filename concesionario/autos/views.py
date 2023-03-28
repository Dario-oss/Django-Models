from django.shortcuts import render

# Create your views here.
def autos(request):
    modelos=['Ford','Kia','Mazda','Nissan','Suzuki','Toyota','Hyundai']
    contexto={'listado':modelos}
    return render (request, 'modelos.html' ,contexto)

def clientes(request):
    cliente=['Cliente 1','Cliente 2','cliente 3']
    contexto={'listado':cliente}
    return render (request, 'clientes.html' ,contexto)