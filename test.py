import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Passo 1: Carregar os Dados
Base_Dados = pd.read_excel('modelosML/RandomForest/dados_diario WEBER LUCAS.xlsx')

# Passo 2: Preparar os Dados
# Supondo que a coluna 'consumo' contém o consumo diário
consumo = Base_Dados['CONSUMO'].values

# Criar features e labels
# Utilizando uma janela deslizante para criar features
def create_features_labels(consumo, window_size):
    X, y = [], []
    for i in range(len(consumo) - window_size):
        X.append(consumo[i:i + window_size])  # Features
        y.append(consumo[i + window_size])    # Label (consumo do próximo dia)
    return np.array(X), np.array(y)

# Definir o tamanho da janela (quantos dias anteriores você usa para prever o próximo)
window_size = 30  # Por exemplo, usar os últimos 7 dias para prever o consumo do próximo dia
X, y = create_features_labels(consumo, window_size)

# Passo 3: Dividir os Dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 4: Treinar o Modelo
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões e avaliar o modelo
previsor = modelo.predict(X_test)
mse = mean_squared_error(y_test, previsor)
print(f"Mean Squared Error: {mse}")


# Exemplo de previsão
def predict_next_day_consumo(modelo, last_days):
    last_days_array = np.array(last_days).reshape(1, -1)
    return modelo.predict(last_days_array)[0]

# Suponha que você queira prever o consumo do dia seguinte com base nos últimos 7 dias
last_7_days = consumo[-window_size:]  # Pegando os últimos 7 dias dos dados
predicted_consumo = predict_next_day_consumo(modelo, last_7_days)
print("Predição do consumo do próximo dia:", predicted_consumo)
