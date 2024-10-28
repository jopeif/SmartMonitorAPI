import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Carregar os dados
Base_Dados = pd.read_excel('/content/dados_diario WEBER LUCAS.xlsx')
Base_Dados.dropna(inplace=True)

consumo = Base_Dados['CONSUMO'].values

def create_features_targets(data, window_size=30):
    features, targets = [], []
    for i in range(len(data) - window_size):
        features.append(data[i:i + window_size])
        targets.append(data[i + window_size])
    return np.array(features), np.array(targets)

x, y = create_features_targets(consumo, window_size=30)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=122)

modelo = XGBRegressor(use_label_encoder=False, eval_metric='mlogloss')
modelo.fit(x_train, y_train)

previsor = modelo.predict(x_test)

def predict_next_number(model, last_numbers, window_size=30):
      last_numbers = np.array(last_numbers).reshape(1, -1)
      return model.predict(last_numbers)[0]

# Exemplo de uso da função
# Obtendo os últimos 30 valores de y para prever o próximo valor
last_30_numbers = y.tail(30).values
predicted_next_number = predict_next_number(modelo, last_30_numbers)
print("Predição do trigésimo primeiro número:", predicted_next_number)

# Salvar o modelo
joblib.dump(modelo, 'modelosML/RandomForest/modeloPreverConsumo.joblib')