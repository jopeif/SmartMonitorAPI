# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


# Carregar base de dados
Base_Dados = pd.read_excel('SmartMonitorAPI/modelosML/RandomForest/consumo_agua.xlsx')

# Remover dados nulos
Base_Dados.dropna(inplace=True)

x = Base_Dados.iloc[:,2:3]
y = Base_Dados['Valor da Fatura(R$)']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(x_train, y_train)

previsor = modelo.predict(x_test)

import joblib

joblib.dump(modelo, 'SmartMonitorAPI/modelosML/RandomForest/modelo.joblib')
