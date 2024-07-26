from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions

from rest_framework.views import APIView

import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import numpy as np

from appSM.serializers import MySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from modelosML.StatisticalAnalysis.StatisticalAnalysis import Statistic_Analysis



class HelloWord(APIView):
    @permission_classes([permissions.IsAuthenticated])
    def get(request):
        data = {"Hello, world!"}
        return Response(data, status=status.HTTP_200_OK)


#ANALISE ESTATÍSTICA#
class Statis_Analys(APIView):
    @permission_classes([permissions.IsAuthenticated])
    @swagger_auto_schema(
        request_body=MySerializer,
        responses={201: openapi.Response('Created', MySerializer)}
    )
    
    def post(self, request):
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data.get('float_list', [])
            response = Statistic_Analysis(data)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Pred_RandomForest(APIView):
    @permission_classes([permissions.IsAuthenticated])
    @swagger_auto_schema(
        request_body=MySerializer,
        responses={201: openapi.Response('Created', MySerializer)}
    )
    def post(request):
        # Random Forest
        # Carregar o modelo ↓
        modelo = joblib.load('.\modelosML\RandomForest\modelo.joblib')
        try:
            data = json.loads(request.body)
            numbers = data.get('id_sensor', [])
            if len(numbers) != 1:
                return JsonResponse({'error': 'A lista deve conter exatamente 1 números.'}, status=400)
            
            # Converte a lista para um array numpy e faz a predição
            numbers_array = np.array(numbers).reshape(1, -1)
            prediction = modelo.predict(numbers_array)[0]
            
            return JsonResponse({'prediction': prediction})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        
def RF():
    return 'RF'

#TRATAMENTO DOS DADOS
# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def dataTreatment(.items):
    
#     for instituition, sensors in request.items():
#         for sensorID, consumption in sensors.items():
#             print(consumption)

class Exemplo(APIView):
    @swagger_auto_schema(
        request_body=MySerializer,
        responses={201: openapi.Response('Created', MySerializer)}
    )
    def post(self, request):
        serializer = MySerializer(data=request.data)