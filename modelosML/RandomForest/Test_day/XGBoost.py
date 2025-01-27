import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model():

    Base_Dados = pd.read_excel('./modelosML/Consumos/dados_diario WEBER LUCAS.xlsx')
    Base_Dados.sort_values(by='DATA', inplace=True)
    consumo = Base_Dados['CONSUMO'].values

    def create_features_targets(data, window_size=30):
        features, targets = [], []
        for i in range(len(data) - window_size):
            features.append(data[i:i + window_size])
            targets.append(data[i + window_size])
        return np.array(features), np.array(targets)

    x, y = create_features_targets(consumo, window_size=30)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=122)

    modelo = XGBRegressor(
        eval_metric='rmse',  # Para regressão, "rmse" é uma métrica adequada
        n_estimators=100,  # Número de árvores
        max_depth=3,  # Profundidade máxima das árvores
        learning_rate=0.01,  # Taxa de aprendizado
        subsample=0.8,  # Subamostragem de dados
        min_child_weight=3,  # Peso mínimo para folhas das árvores
        gamma=0.5,  # Regularização para evitar overfitting
        colsample_bytree=0.7  # Subamostragem de colunas para cada árvore
    )
    modelo.fit(x_train, y_train)
    
    # Avaliação
    y_pred = modelo.predict(x_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE no conjunto de teste: {rmse}")

    return modelo

def predict_next_day(modelo, last_numbers, window_size=30):
    if len(last_numbers) != window_size:
        raise ValueError(f"O tamanho de last_numbers deve ser {window_size}, mas é {len(last_numbers)}.")
    
    last_numbers = np.array(last_numbers).astype(float).reshape(1, -1)
    return modelo.predict(last_numbers)[0]

# y_pred = modelo.predict(x_test)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# print(f"RMSE no conjunto de teste: {rmse}")
model_trained_day = train_model()





##*Avaliar para achar melhorar parametros*##
# from sklearn.model_selection import RandomizedSearchCV
# import numpy as np

# # Definir o grid de parâmetros para busca aleatória
# param_dist = {
#     'n_estimators': [100, 200, 300, 500],
#     'learning_rate': [0.01, 0.05, 0.1, 0.3],
#     'max_depth': [3, 5, 7, 9],
#     'subsample': [0.7, 0.8, 0.9, 1.0],
#     'colsample_bytree': [0.7, 0.8, 1.0],
#     'gamma': [0, 0.1, 0.3, 0.5],
#     'min_child_weight': [1, 3, 5],
# }

# # Usar RandomizedSearchCV
# random_search = RandomizedSearchCV(estimator=modelo, param_distributions=param_dist, 
#                                 n_iter=100, scoring='neg_mean_squared_error', 
#                                 cv=5, n_jobs=-1, verbose=2, random_state=42)
# random_search.fit(x_train, y_train)

# # Exibir os melhores parâmetros
# print("Melhores parâmetros:", random_search.best_params_)