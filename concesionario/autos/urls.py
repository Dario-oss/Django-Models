from django.urls import path
from . import views

urlpatterns = [
    path('', views.autos,name='autos'),
    path('Clientes/',views.clientes,name='clientes'),
    
]


