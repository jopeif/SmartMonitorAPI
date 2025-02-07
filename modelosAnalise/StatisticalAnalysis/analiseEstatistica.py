from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pandas as pd


## Essa é outra abordagem de análise estatistica

def analise_estatistica(data):
    try:
        # Criação do DataFrame
        df = pd.DataFrame({"Data": data['Data'], "Consumo": data['Consumo']})
        df["Média Móvel"] = df["Consumo"].rolling(window=7).mean()
        df["Desvio Padrão"] = df["Consumo"].rolling(window=7).std()
        
        # Criação das bandas
        for i in range(1, 4):
            df[f"Banda Inferior {i}"] = df["Média Móvel"] - (i * df["Desvio Padrão"])
            df[f"Banda Superior {i}"] = df["Média Móvel"] + (i * df["Desvio Padrão"])
        
        # classificação do consumo
        classificacoes = []
        for i, row in df.iterrows():
            consumo = row["Consumo"]
            media_movel = row["Média Móvel"]
            banda_inferior1 = row["Banda Inferior 1"]
            banda_superior1 = row["Banda Superior 1"]
            banda_superior2 = row["Banda Superior 2"]
            
            if consumo <= banda_inferior1:
                classificacao = "Economia Máxima"
            elif banda_inferior1 < consumo <= media_movel:
                classificacao = "Uso Eficiente"
            elif media_movel < consumo <= banda_superior1:
                classificacao = "Consumo Moderado"
            elif banda_superior1 < consumo <= banda_superior2:
                classificacao = "Uso Elevado"
            elif consumo > banda_superior2:
                classificacao = "Consumo Excessivo"
            else:
                classificacao = "Sem classificação"
                
            classificacoes.append(classificacao)
            
        # Adiciona as classificações ao DataFrame
        df["Classificação"] = classificacoes
        
        
        return df.fillna("").to_dict(orient="records")
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)