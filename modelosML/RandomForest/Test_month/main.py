import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model():
    Base_Dados = pd.read_excel('./modelosML/Consumos/IFCE - Unidades.xlsx')
    Base_Dados.sort_values(by='DATA', inplace=True)
    consumo = Base_Dados['CONSUMO'].values

    # Criar a série temporal de features e target
    def create_features_targets(data, window_size=12):
        features, targets = [], []
        for i in range(len(data) - window_size):
            features.append(data[i:i + window_size])
            targets.append(data[i + window_size])
        return np.array(features), np.array(targets)

    x, y = create_features_targets(consumo, window_size=12)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=66)

    modelo = RandomForestRegressor(n_estimators=500, random_state=42)
    modelo.fit(x_train, y_train)

    y_pred = modelo.predict(x_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE no conjunto de teste: {rmse}")

    return modelo

def predict_next_day(modelo, last_numbers, window_size=12):
    
    last_numbers = pd.read_excel('./modelosML/Consumos/IFCE - Unidades.xlsx', 'Tabuleiro do Norte')
    
    if len(last_numbers) != window_size:
        raise ValueError(f"O tamanho de last_numbers deve ser {window_size}, mas é {len(last_numbers)}.")
    
    last_numbers = np.array(last_numbers).astype(float).reshape(1, -1)
    return modelo.predict(last_numbers)[0]

model_trained_day = train_model()
