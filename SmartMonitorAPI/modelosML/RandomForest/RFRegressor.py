import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from django.http import JsonResponse


def RF():
    Base_Dados = pd.read_excel('https://drive.google.com/uc?export=download&id=1cnPo6RCGZDxL2ZfDCekEAzULVjbtHBN-', sheet_name='Planilha1')

    Sensor = {
        'if14125gfdf':['0.1314112','0.122425']
    }

    Sensor['if14125gfdf']

    