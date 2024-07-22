import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from django.http import JsonResponse

class RandomForest:
    # Carregar base de dados
    Base_Dados = pd.read_excel('https://drive.google.com/uc?export=download&id=1cnPo6RCGZDxL2ZfDCekEAzULVjbtHBN-', sheet_name='Planilha1')

    # Remover dados nulos
    Base_Dados.dropna(inplace=True)
    
    