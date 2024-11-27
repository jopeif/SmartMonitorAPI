import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib


# Carregar os dados
Base_Dados = pd.read_excel('modelosML/Consumos/dados_diario WEBER LUCAS.xlsx')

# Remover valores nulos
Base_Dados.dropna(inplace=True)

consumo = Base_Dados['CONSUMO'].values

# Criar a série temporal de features e target
def create_features_targets(data, window_size=30):
    features, targets = [], []
    for i in range(len(data) - window_size):
        features.append(data[i:i + window_size])
        targets.append(data[i + window_size])
    return np.array(features), np.array(targets)

x, y = create_features_targets(consumo, window_size=30)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=66)

modelo = RandomForestRegressor(n_estimators=1000, random_state=42)
modelo.fit(x_train, y_train)

previsor = modelo.predict(x_test)

def predict_next_number(model, last_30_numbers):
    last_30_numbers = np.array(last_30_numbers).reshape(1, 30)
    return model.predict(last_30_numbers)[0]

# Exemplo de uso da função
# Obtendo os últimos 30 valores de consumo
last_30_numbers = consumo[-30:]
predicted_next_number = predict_next_number(modelo, last_30_numbers)
print("Predição do trigésimo primeiro número:", predicted_next_number)

# Salvar o modelo
joblib.dump(modelo, 'modelosML/RandomForest/Test/modeloPreverConsumo.joblib')
