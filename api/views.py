from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import Beacons, Puntodeinteres
from api.serializers import BeaconsSerializer, PuntodeinteresSerializer
from rest_framework.decorators import api_view
# Create your views here.

##############
# PUNTOS DE INTERÉS
######################################################
@api_view(['GET','POST','DELETE'])
def puntodeinteres_list(request):
    if request.method == 'GET':
        puntosdeinteres = Puntodeinteres.objects.all()

        '''titulo = request.GET.get('titulo',None)
        if titulo is not None:
            puntosdeinteres = puntosdeinteres.filter(title__icontains=titulo)'''

        puntosdeinteres_serializer = PuntodeinteresSerializer(puntosdeinteres, many=True)
        return JsonResponse(puntosdeinteres_serializer.data, safe=False)
    elif request.method == 'POST':
        puntodeinteres_data = JSONParser().parse(request)
        puntodeinteres_serializer = PuntodeinteresSerializer(data=puntodeinteres_data)
        if puntodeinteres_serializer.is_valid():
            puntodeinteres_serializer.save()
            return JsonResponse(puntodeinteres_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(puntodeinteres_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Puntodeinteres.objects.all().delete()
        return JsonResponse({'message':'ok'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def puntodeinteres_detail(request,pk):
    try:
        puntodeinteres = Puntodeinteres.objects.get(pk=pk)
    except Puntodeinteres.DoesNotExist:
        return JsonResponse({'message':'El Punto de Interés no existe.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        puntodeinteres_serializer = PuntodeinteresSerializer(puntodeinteres)
        return JsonResponse(puntodeinteres_serializer.data)
    elif request.method == 'PUT':
        puntodeinteres_data = JSONParser().parse(request)
        puntodeinteres_serializer = PuntodeinteresSerializer(puntodeinteres, data=puntodeinteres_data)
        if puntodeinteres_serializer.is_valid():
            puntodeinteres_serializer.save()
            return JsonResponse(puntodeinteres_serializer.data)
        return JsonResponse(puntodeinteres_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        puntodeinteres.delete()
        return JsonResponse({'message':'ok'})

###########################
# BEACONS
#############################################################
@api_view(['GET','POST','DELETE'])
def puntodeinteres_beacons_list(request):
    if request.method == 'GET':
        beacons = Beacons.objects.all()

        beacons_serializer = BeaconsSerializer(beacons, many=True)
        return JsonResponse(beacons_serializer.data, safe=False)
    elif request.method == 'POST':
        beacons_data = JSONParser().parse(request)
        beacons_serializer = BeaconsSerializer(data=beacons_data)
        if beacons_serializer.is_valid():
            beacons_serializer.save()
            return JsonResponse(beacons_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(beacons_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Beacons.objects.all().delete()
        return JsonResponse({'message':'ok'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def puntodeinteres_beacons_detail(request,pk):
    try:
        beacons = Beacons.objects.get(pk=pk)
    except Beacons.DoesNotExist:
        return JsonResponse({'message':'ok'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        conexiones = beacons.conexiones
        conexiones += 1
        Beacons.objects.filter(id=beacons.id).update(conexiones=conexiones)
        beacons_serializer = BeaconsSerializer(beacons)
        return JsonResponse(beacons_serializer.data)
    elif request.method == 'PUT':
        beacons_data = JSONParser().parse(request)
        beacons_serializer = BeaconsSerializer(beacons, data=beacons_data)
        if beacons_serializer.is_valid():
            beacons_serializer.save()
            return JsonResponse(beacons_serializer.data)
        return JsonResponse(beacons_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        beacons.delete()
        return JsonResponse({'message':'ok'})
