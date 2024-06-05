from django.urls import path
from EntregaApp.views import productos

urlpatterns = [
    path('productos/', productos, name='productos'),

]
