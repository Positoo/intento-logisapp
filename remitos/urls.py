from django.urls import path
from .views import lista_remitos

urlpatterns = [
    path('remitos/', lista_remitos, name='lista_remitos'),
]
