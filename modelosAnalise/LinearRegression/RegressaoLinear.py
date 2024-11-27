import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class LinearRegressionPrediction:
    def __init__(self):
        self.model = None

    # Predição diária
    def train(self, data):
        x = np.arange(len(data)).reshape(-1, 1)
        y = np.array(data)
        self.model = LinearRegression()
        self.model.fit(x, y)

    def prediction(self, consumos):
        if self.model is None:
            raise ValueError("O modelo não foi treinado.")

        dadosConsumo = np.array(consumos).reshape(1, -1)
        return self.model.predict(dadosConsumo)[0]
