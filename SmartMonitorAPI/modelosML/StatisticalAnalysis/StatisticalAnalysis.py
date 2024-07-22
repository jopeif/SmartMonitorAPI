from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import numpy as np

def StatisticalAnalysis(request):
    try:
        # Verificar se os dados foram fornecidos na requisição
        if "data" not in request.data:
            return Response({"error": "Os dados não foram fornecidos."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Obter os dados fornecidos pelo usuário
        input_data = request.data['data']
        
        # Verificar se a quantidade de dados fornecidos é igual a 30
        if len(input_data) != 30:
            return Response({"error": "É necessário fornecer exatamente 30 valores de consumo."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Converter os dados fornecidos em um array numpy
        data = np.array(input_data)
        
        # Calcular a Média Móvel Simples (SMA)
        sma = np.mean(data)
        
        # Calcular o Desvio Padrão
        std_dev = np.std(data)
        
        # Calcular as Bandas de Bollinger
        upper_band = sma + (2 * std_dev)
        lower_band = sma - (2 * std_dev)
        
        # Classificar o consumo atual
        current_consumption = data[-1]
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
        
        return Response({
            "current_consumption": float(current_consumption),
            "classification": classification,
            "sma": float(sma),
            "upper_band": float(upper_band),
            "lower_band": float(lower_band)
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)