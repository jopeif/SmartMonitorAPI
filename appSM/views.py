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

from django.http import JsonResponse

from modelosML.StatisticalAnalysis.StatisticalAnalysis import Statistic_Analysis
from modelosML.RandomForest.Test_day.main import predict_next_day, model_trained_day
from modelosML.RandomForest.Test_month.main import predict_next_month, model_trained_month
from JSONs import test_json

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



class Next_day(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=MySerializer,
        responses={201: openapi.Response('Created', MySerializer)}
    )

    def post(self, request):
        try:
            jsondata = json.loads(request.body)
         
            test_json.model_json(jsondata)
            values=test_json.valores

            if len(values) < 30:
                print(f"Dados insuficientes para prever o consumo do sensor .")
            
            prediction = predict_next_day(model_trained_day, values[-30:])

            return JsonResponse({'Previsão próx. dia': float(prediction)})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class Next_month(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=MySerializer,
        responses={201: openapi.Response('Created', MySerializer)}
    )

    def post(self, request):
        try:
            jsondata = json.loads(request.body)
         
            test_json.model_json(jsondata)
            values=test_json.valores

            if len(values) < 12:
                print(f"Dados insuficientes para prever o consumo do sensor .")
            
            prediction = predict_next_day(model_trained_day, values[-12:])
            
            return JsonResponse({'Previsão próx. mês': float(prediction)})
        
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
