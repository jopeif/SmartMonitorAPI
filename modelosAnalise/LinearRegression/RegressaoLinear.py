import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Descontinuado
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


class LinearRegression_Acumulado:
    def __init__(self):
        self.model = None

    def train(self, data):
        x = np.arange(len(data)).reshape(-1, 1)
        y = np.array(data['Acumulado'])
        self.model = LinearRegression()
        self.model.fit(x, y)
        # return f"valores de x: {x}, y: {y}"

    def prediction(self, indices: int | list[int]) -> int | np.ndarray:
        if self.model is None:
            raise ValueError("O modelo não foi treinado.")

        pred = self.model.predict(np.array(indices).reshape(-1, 1))

        if isinstance(indices, int):
            return pred[0]
        
        return pred