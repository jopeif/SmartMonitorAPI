import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class RandomForestPrediction:
    def __init__(self, n_estimators=1000, random_state=42):
        self.n_estimators = n_estimators
        self.random_state = random_state
        self.model = None


    @staticmethod
    def create_features_targets(data, window_size=29):
        """
        Cria as features e os targets a partir dos dados.
        """
        features, targets = [], []
        for i in range(len(data) - window_size):
            features.append(data[i:i + window_size])
            targets.append(data[i + window_size])
        return np.array(features), np.array(targets)
    

    # Treinar modelo
    def train(self, data, window_size=29):
        x, y = self.create_features_targets(data, window_size)
        self.model = RandomForestRegressor(n_estimators = self.n_estimators, random_state = self.random_state)
        self.model.fit(x, y)
    

    # Predição do modelo

    def prediction(self, consumos):
        if self.model is None:
            raise ValueError("O modelo não foi treinado.")
        dadosConsumo = np.array(consumos).reshape(1, -1)
        return self.model.predict(dadosConsumo)[0]