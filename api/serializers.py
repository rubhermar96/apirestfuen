from rest_framework import serializers
from api.models import Beacons, Puntodeinteres

class PuntodeinteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntodeinteres
        fields = (
            'id',
            'titulo',
            'imagen_destacada',
            'horario',
            'descripcion',
            'imagenes',
            'videos',
        )

class BeaconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacons
        fields = (
            'id',
            'nombre',
            'puntodeinteres',
            'texto',
            'conexiones',
        )