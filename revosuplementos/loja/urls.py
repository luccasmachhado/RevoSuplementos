from django.urls import path
from .views import home, reservar_produto

urlpatterns = [
    path('', home, name='home'),
    path('reservar/<int:produto_id>/', reservar_produto, name='reservar'),
]