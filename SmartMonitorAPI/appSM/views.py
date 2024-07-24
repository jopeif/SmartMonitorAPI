from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
import json


from modelosML.StatisticalAnalysis.StatisticalAnalysis import Statistic_Analysis


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def helloword(request):
    data = {"Hello, world!"}
    return Response(data, status=status.HTTP_200_OK)


#ANALISE ESTATÍSTICA
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def statis_analy(request):
    response = Statistic_Analysis(request)
    return response

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def RF():
    return 'RF'

#TRATAMENTO DOS DADOS
# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def dataTreatment(.items):
    
#     for instituition, sensors in request.items():
#         for sensorID, consumption in sensors.items():
#             print(consumption)