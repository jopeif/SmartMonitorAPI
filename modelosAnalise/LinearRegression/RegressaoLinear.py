import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class LinearRegressionPrediction:
    def __init__(self):
        self.model = None

    def train(self, data):
        x = np.arange(len(data)).reshape(-1, 1)
        y = np.array(data['Consumo'])
        self.model = LinearRegression()
        self.model.fit(x, y)

    def prediction(self, indicePredicao):
        if self.model is None:
            raise ValueError("O modelo não foi treinado.")

        valorPredicao = np.array(indicePredicao).reshape(1, -1)
        return self.model.predict(valorPredicao)[0]
