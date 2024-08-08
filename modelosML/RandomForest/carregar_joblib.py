import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Carregar os dados
Base_Dados = pd.read_excel('modelosML/Consumos/RandomForest/dados_diario WEBER LUCAS.xlsx')

# Remover valores nulos
Base_Dados.dropna(inplace=True)

# Separar features e target
x = Base_Dados.iloc[:, :1]  # Primeira coluna como feature
y = Base_Dados.iloc[:, 1]   # Segunda coluna como target

# Dividir os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=66)

# Treinar o modelo
modelo = RandomForestRegressor(n_estimators=1000, random_state=42)
modelo.fit(x_train, y_train)

# Fazer previsões no conjunto de teste
previsor = modelo.predict(x_test)

# Função para prever o próximo número com base nos últimos 30 números
def predict_next_number(model, last_30_numbers):
    last_30_numbers = np.array(last_30_numbers).reshape(1, 30)  # Ajustar para formato (1, 30)
    return model.predict(last_30_numbers)[0]

# Exemplo de uso da função
# Obtendo os últimos 30 valores de y para prever o próximo valor
last_30_numbers = y.tail(30).values
predicted_next_number = predict_next_number(modelo, last_30_numbers)
print("Predição do trigésimo primeiro número:", predicted_next_number)

# Salvar o modelo
#joblib.dump(modelo, 'modelosML/RandomForest/modeloPreverConsumo.joblib')