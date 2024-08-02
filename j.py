import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

Base_Dados = pd.read_excel('modelosML/RandomForest/dados_diario WEBER LUCAS.xlsx')

Base_Dados.dropna(inplace=True)

x = Base_Dados.iloc[:,0:1]  
y = Base_Dados.iloc[:, 1]  

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(x_train, y_train)

previsor = modelo.predict(x_test)

mse = mean_squared_error(y_test, previsor)
print(f"Mean Squared Error: {mse}")


def predict_next_number(model, last_30_numbers):
    last_30_numbers = np.array(last_30_numbers).reshape(-1, 1)
    return model.predict(last_30_numbers)[0]


last_30_numbers = y.tail(30).values.reshape(-1, 1)
predicted_next_number = predict_next_number(modelo, last_30_numbers)
print("Predição do trigésimo primeiro número:", predicted_next_number)


import joblib

joblib.dump(modelo, 'modelosML/RandomForest/modeloPreverConsumo.joblib')