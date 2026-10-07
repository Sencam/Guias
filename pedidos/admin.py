from django.contrib import admin
from .models import Cliente, Servicio
# Register your models here.

@Admin.register(Servicio)
Class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "duracion_min")
    search_fields = ("nombre",)
    ordering      = ("nombre",)

