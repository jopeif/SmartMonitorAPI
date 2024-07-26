from rest_framework.response import Response
from rest_framework import status
import numpy as np
from datetime import datetime
from appSM.serializers import MySerializer

def Statistic_Analysis(data):
    try:
        # Verificar se os dados foram fornecidos
        if not data:
            return Response({"error": f"Os dados não foram fornecidos.\n {data}"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verificar se a quantidade de dados fornecidos é igual a 30
        if len(data) != 30:
            return Response({"error": "É necessário fornecer exatamente 30 valores de consumo."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Converter os dados fornecidos em um array numpy
        data_array = np.array(data)
        
        # Calcular a Média Móvel Simples (SMA)
        sma = np.mean(data_array)
        
        # Calcular o Desvio Padrão
        std_dev = np.std(data_array)
        
        # Calcular as Bandas de Bollinger
        upper_band = sma + (2 * std_dev)
        lower_band = sma - (2 * std_dev)
        
        # Classificar o consumo atual
        current_consumption = data_array[-1]
        if current_consumption < lower_band:
            classification = "MUITO BAIXO"
        elif current_consumption < sma:
            classification = "BAIXO"
        elif current_consumption < upper_band:
            classification = "NORMAL"
        elif current_consumption < upper_band + std_dev:
            classification = "ALTO"
        else:
            classification = "MUITO ALTO"


        current_datetime = datetime.now()


        timestamp_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        
        return Response({
            "classification": classification,
            "timestamp": timestamp_str
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
