from django.contrib import admin
from .models import Beacons, Puntodeinteres

# Register your models here.
@admin.register(Puntodeinteres)
class PuntodeinteresAdmin(admin.ModelAdmin):
    list_display = ("titulo","pk")

@admin.register(Beacons)
class BeaconsAdmin(admin.ModelAdmin):
    list_display = ("pk","nombre","puntodeinteres")
