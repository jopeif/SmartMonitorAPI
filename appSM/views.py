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

from modelosML.StatisticalAnalysis.StatisticalAnalysis import analise_estatistica



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
            response = analise_estatistica(data)
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
            # Decodificar o corpo da requisição
            data = json.loads(request.body)
            numbers = data.get('id_sensor', [])
            
            # Validar o comprimento da lista
            if len(numbers) != 30:
                return JsonResponse({'error': 'A lista deve conter exatamente 30 números.'}, status=400)
            
            # Verificar se todos os elementos podem ser convertidos para float
            try:
                numbers = [float(num) for num in numbers]
            except ValueError:
                return JsonResponse({'error': 'Todos os valores devem ser números.'}, status=400)

            # Carregar o modelo
            modelo = joblib.load('modelosML/RandomForest/modeloPreverConsumo.joblib')
            
            # Transformar os números em um array 2D com forma (1, 30)
            numbers_array = np.array(numbers).reshape(1, -1)
            
            # Fazer a previsão e converter para float
            prediction = float(modelo.predict(numbers_array)[0])
            
            # Retornar a previsão em JSON
            return JsonResponse({'Predição do próximo consumo': prediction})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            