from django.urls import path
from .views import lista_remitos, crear_remito

urlpatterns = [
    path('remitos/', lista_remitos, name='lista_remitos'),
    path('remitos/nuevo/', crear_remito, name='crear_remito'),
]
