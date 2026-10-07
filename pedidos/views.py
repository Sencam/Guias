from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def lista_pedidos(request):
    return HttpResponse(
        "Pedidos del food truck"
    )
