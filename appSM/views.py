import json
import joblib
import numpy as np
import pandas as pd
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
from modelosML.RandomForest.Test.test import train_model, predict_next_number

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
            modelo = joblib.load('.modelosML/RandomForest/modeloPreverConsumo.joblib')
            
            # Transformar os números em um array 2D com forma (1, 30)
            numbers_array = np.array(numbers).reshape(1, -1)
            
            # Fazer a previsão
            prediction = modelo.predict(numbers_array)[0]

            prediction = float(prediction)
            
            return JsonResponse({'Predição do próximo consumo': prediction})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        

class TestRF_Regressor(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
    request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'Instituição': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            additional_properties=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                additional_properties=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    additional_properties=openapi.Schema(
                        type=openapi.TYPE_NUMBER,
                        nullable=True
                    )
                )
            )
        )
    },
    description="Dicionário com as instituições, sensores e valores associados às datas."
    )
    )

    
    def post(self, request):
        try:
            # Carregar e validar o JSON
            jsondata = json.loads(request.body)

            jsondata_reestruturado = {}

            json_prediction = {}

            # Iterar pelas instituições no JSON
            for instituicao, sensores in jsondata.items():
                json_prediction[instituicao] = {}
                for sensor, leituras in sensores.items():
                    json_prediction[instituicao][sensor] = {}

            # Iterar pelas instituições no JSON
            for instituicao, sensores in jsondata.items():
                jsondata_reestruturado[instituicao] = {}
                for sensor, leituras in sensores.items():

                    # Criar DataFrame com os dados do sensor
                    df = pd.DataFrame.from_dict(leituras, orient="index", columns=["values"])

                    # Preencher valores nulos com interpolação linear
                    df["values"] = df["values"].interpolate(method="linear", limit_direction="both")

                    # Converter de volta para dicionário
                    jsondata_reestruturado[instituicao][sensor] = df["values"].to_dict()

            for sensor in sensores:
                modelo_trained = train_model()

                keys=jsondata_reestruturado[instituicao][sensor]

                # Extrair apenas os valores, ignorando as datas
                values = list(keys.values())

                if len(values) < 30:
                    print(f"Dados insuficientes para prever o consumo do sensor {sensor} na instituição {instituicao}.")
                    continue

                
                prediction = predict_next_number(modelo_trained, values[-30:])
                json_prediction[instituicao][sensor] = float(prediction)

            return JsonResponse(json_prediction)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    
    
from modelosML.StatisticalAnalysis.analiseEstatistica import analise_estatistica

class calcular_analise_estatistica(APIView):
    
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
            response = analise_estatistica(data)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
