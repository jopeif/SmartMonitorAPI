from rest_framework.response import Response
from rest_framework import status
import numpy as np
from datetime import datetime
from appSM.serializers import MySerializer
import pandas as pd


## Essa é outra abordagem de análise estatistica

def analise_estatistica(data):
    try:
        # Verificar se os dados foram fornecidos
        if not data:
            return Response({"error": f"Os dados não foram fornecidos.\n {data}"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verificar se a quantidade de dados fornecidos é igual a 30
        if len(data) != 30:
            return Response({"error": "É necessário fornecer exatamente 30 valores de consumo."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Converter os dados fornecidos em um array numpy
        data_array = np.array(data)
        
        # Criação do DataFrame
        df = pd.DataFrame({"Consumo": data_array})
        df["Média Móvel"] = df["Consumo"].rolling(window=7).mean()
        df["Desvio Padrão"] = df["Consumo"].rolling(window=7).std()
        
        for i in range(1, 4):
            df[f"Banda Inferior {i}"] = df["Média Móvel"] - (i * df["Desvio Padrão"])
            df[f"Banda Superior {i}"] = df["Média Móvel"] + (i * df["Desvio Padrão"])
        
        resposta = df.fillna("").to_dict(orient="records")
        return Response(resposta, status=status.HTTP_200_OK)
            
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)