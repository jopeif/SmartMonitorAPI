from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
import json


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import numpy as np

from modelosML.StatisticalAnalysis.StatisticalAnalysis import Statistic_Analysis



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def helloword(request):
    data = {"Hello, world!"}
    return Response(data, status=status.HTTP_200_OK)


#ANALISE ESTATÍSTICA#
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def statis_analy(request):
    response = Statistic_Analysis(request)
    return response

# Random Forest
# Carregar o modelo ↓
modelo = joblib.load('.\modelosML\RandomForest\modelo.joblib')

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def pred_RandomForest(request):

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
