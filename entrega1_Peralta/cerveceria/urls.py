from django.urls import path
from . import views


urlpatterns = [

    path("", views.inicio), 
    path("inicio", views.inicio ),
    path("alta_estilos", views.estilosFormulario),
    path("estilos_formulario", views.estilosFormulario),
    path("productos_formulario", views.productosFormulario),
    path("staff_formulario", views.staffFormulario),
    path("lista_estilos", views.lista_estilos),
    path("lista_staff", views.lista_staff),
    path("lista_productos", views.lista_productos),
    path("busquedaAlcohol", views.busquedaAlcohol, name = "busquedaAlcohol"),
    path("buscar/", views.buscar)
    
]