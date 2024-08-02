import json
import joblib
import numpy as np
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from appSM.serializers import MySerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import JsonResponse

from modelosML.StatisticalAnalysis.StatisticalAnalysis import Statistic_Analysis



#ANALISE ESTATÍSTICA#
class Statis_Analys(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=MySerializer,
        responses={201: openapi.Response('Created', MySerializer)}
    )
    
    def post(self, request):
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data.get('data', [])
            print(data)
            response = Statistic_Analysis(data)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Pred_RandomForest(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_sensor': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_NUMBER))
            }
        ),
        responses={200: openapi.Response('Success', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'prediction': openapi.Schema(type=openapi.TYPE_NUMBER)}))}
    )
    def post(self, request):
        try:
            data = json.loads(request.body)
            numbers = data.get('id_sensor', [])
            if len(numbers) != 30:
                return JsonResponse({'error': 'A lista deve conter exatamente 30 números.'}, status=400)
            
            # Carregar o modelo
            modelo = joblib.load('./modelosML/RandomForest/modeloPreverConsumo.joblib')
            
            # Transformar os números em um array 2D
            numbers_array = np.array(numbers).reshape(-1, 1)
            
            # Fazer a previsão
            prediction = modelo.predict(numbers_array)[0]
            
            return JsonResponse({'Predição do próximo consumo': prediction})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        

def RF():
    return {"RF"}

#TRATAMENTO DOS DADOS
# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def dataTreatment(.items):
    
#     for instituition, sensors in request.items():
#         for sensorID, consumption in sensors.items():
#             print(consumption)

class Exemplo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"Funcionando!"})