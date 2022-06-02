from django.shortcuts import render
from django.http import HttpResponse
from cerveceria.models import *

# Create your views here.


"""
def alta_estilos(request):
    
    estilo = Estilos(nombre = "IPA" , ibu = 55 , alcohol = 6 , cuerpo = "Medio", amargor = "Intenso", aroma = "Citrico", temp_cons = 7)
    estilo.save()
    estilo = Estilos(nombre = "BROWN ALE" , ibu = 25, alcohol = 5 , cuerpo = "Medio", amargor = "Medio", aroma = "Caramelo", temp_cons = 8)
    estilo.save()
    estilo = Estilos(nombre = "PORTER" , ibu = 40, alcohol = 6 , cuerpo = "Pleno", amargor = "Medio", aroma = "Malta", temp_cons = 6)
    estilo.save()
    return HttpResponse("Todo ok alta estilos")
"""
def estilosFormulario(request):    

    if request.method == 'POST':

        estilo = Estilos(nombre = request.POST["nombre"] , ibu = request.POST["ibu"] , alcohol = request.POST["alcohol"]  , cuerpo = request.POST["cuerpo"] , amargor = request.POST["amargor"] , aroma = request.POST["aroma"] , temp_cons = request.POST["temp_cons"] )
        estilo.save()

        return render(request, "inicio.html")
   
    return render(request, "estilos_formulario.html")

def lista_estilos(request):
    estilos = Estilos.objects.all()
    info = {"info": estilos}
    
    return render(request , "lista_estilos.html" , info)

def inicio(request):
    return render(request, "inicio.html")



def busquedaAlcohol(request):

    return render(request, "busquedaAlcohol.html" )

def buscar(request):
    
    if request.GET["alcohol"]:
        alcohol = request.GET["alcohol"]
        estilos = Estilos.objects.filter(alcohol__icontains=alcohol)

        return render(request, "resultadoBusqueda.html", {"estilos": estilos, "alcohol": alcohol})
    else:
        respuesta = "No se ingresaron datos"
    
    return HttpResponse(respuesta)



def productosFormulario(request):    

    if request.method == 'POST':

        producto = Productos(nombre = request.POST["nombre"] , tipo_producto = request.POST["tipo_producto"] , fecha_registro = request.POST["fecha_registro"] )
        producto.save()

        return render(request, "inicio.html")
   
    return render(request, "productos_formulario.html")


def lista_productos(request):
    producto = Productos.objects.all()
    info = {"info": producto}
    
    return render(request , "lista_productos.html" , info)

def lista_staff(request):
    staff = Staffs.objects.all()
    info = {"info": staff}
    
    return render(request , "lista_staff.html" , info)



def staffFormulario(request):    

    if request.method == 'POST':

        staff = Staffs(nombre = request.POST["nombre"] , apellido = request.POST["apellido"], cargo = request.POST["cargo"] , fecha_ingreso = request.POST["fecha_ingreso"] )
        staff.save()

        return render(request, "inicio.html")
   
    return render(request, "staff_formulario.html")
