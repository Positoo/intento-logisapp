from django.urls import path
from .views import lista_remitos, crear_remito, editar_remito, eliminar_remito

urlpatterns = [
    path('remitos/', lista_remitos, name='lista_remitos'),
    path('remitos/nuevo/', crear_remito, name='crear_remito'),
    path('remitos/editar_remito/<int:id>', editar_remito, name='editar_remito'),
    path('remitos/eliminar_remito/<int:id>', eliminar_remito, name='eliminar_remito'),
]
