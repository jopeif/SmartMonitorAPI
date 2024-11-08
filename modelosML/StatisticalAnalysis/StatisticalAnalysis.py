from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pandas as pd
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

        # Calcular a Média Móvel Simples (SMA) com janela de 5
        window_size = 5
        sma = pd.Series(data_array).rolling(window=window_size).mean()  # Aqui, sma será um pandas Series

        # Calcular o Desvio Padrão
        std_dev = np.std(data_array)

        # Calcular as Bandas de Bollinger para 3 níveis de desvio padrão
        upper_band_1 = sma + (1 * std_dev)
        lower_band_1 = sma - (1 * std_dev)

        upper_band_2 = sma + (2 * std_dev)
        lower_band_2 = sma - (2 * std_dev)

        upper_band_3 = sma + (3 * std_dev)
        lower_band_3 = sma - (3 * std_dev)

        # Classificar o consumo atual
        current_consumption = data_array[-1]
        if current_consumption == 0:
            classification = "MUITO BAIXO"
        elif current_consumption < lower_band_2.iloc[-1]:  
            classification = "MUITO BAIXO"
        elif current_consumption < sma.iloc[-1]:
            classification = "BAIXO"
        elif current_consumption < upper_band_2.iloc[-1]:
            classification = "NORMAL"
        elif current_consumption < upper_band_2.iloc[-1] + std_dev:
            classification = "ALTO"
        else:
            classification = "MUITO ALTO"

        # Obter a data e hora atual
        current_datetime = datetime.now()
        timestamp_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Preparar as camadas de bandas para cada ponto
        bands_data = []
        for i in range(len(data_array)):
            # Preencher as bandas com None até que a janela de 5 dados esteja completa
            if i < window_size - 1:
                bands_data.append({
                    "data_point": data_array[i],
                    "lower_band_1": None,
                    "upper_band_1": None,
                    "lower_band_2": None,
                    "upper_band_2": None,
                    "lower_band_3": None,
                    "upper_band_3": None
                })
            else:
                bands_data.append({
                    "data_point": data_array[i],
                    "lower_band_1": lower_band_1.iloc[i],
                    "upper_band_1": upper_band_1.iloc[i],
                    "lower_band_2": lower_band_2.iloc[i],
                    "upper_band_2": upper_band_2.iloc[i],
                    "lower_band_3": lower_band_3.iloc[i],
                    "upper_band_3": upper_band_3.iloc[i]
                })

        # Retornar a resposta com as bandas de Bollinger para cada ponto
        return Response({
            "classification": classification,
            "timestamp": timestamp_str,
            "current_consumption": current_consumption,
            "bands_data": bands_data  # Aqui estão as camadas das bandas para cada ponto
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
