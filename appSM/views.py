import json
from modelosAnalise.tratamento_dados import Tratamentodados
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from appSM.serializers import MySerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import JsonResponse


# Serviço predição
from modelosAnalise.RandomForest.randomforest import RandomForestPrediction
from modelosAnalise.LinearRegression.RegressaoLinear import LinearRegressionPrediction

class Analise_Predicao(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(type=openapi.TYPE_NUMBER)
        ),
        responses={200: openapi.Response('Success', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'prediction': openapi.Schema(type=openapi.TYPE_NUMBER)}))}
    )

    def post(self, request):
        try:
            data = json.loads(request.body)

            tratamento_dados = Tratamentodados()
            dados_dataframe = tratamento_dados.tratamento(data)

            if len(dados_dataframe) != 30:
                return JsonResponse({'error': 'A lista deve conter exatamente 30 dados de consumo.'}, status=400)
            

            modelo = LinearRegressionPrediction()

            # Treinar modelo
            modelo.train(dados_dataframe)

            # Realizar predição
            previsao = modelo.prediction(30)

            return JsonResponse({'Predição do próximo consumo': previsao}, status=status.HTTP_200_OK)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    
# Serviço classificação 
from modelosAnalise.StatisticalAnalysis.analiseEstatistica import analise_estatistica

class calcular_analise_estatistica(APIView):
    
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        request_body=MySerializer,
        responses={201: openapi.Response('Classificado', MySerializer)}
    )
    
    def post(self, request):
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data.get('data', [])
            print(data)
            response = analise_estatistica(data)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
