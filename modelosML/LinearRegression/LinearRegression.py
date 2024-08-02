import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump, load


def train(json_data):
    data = json.loads(json_data)
    df = pd.DataFrame(data)

    X = df.iloc[:, :-1].values  # Supondo que todas as colunas menos a última são features
    y = df.iloc[:, -1].values   # Supondo que a última coluna é o target
    model = LinearRegression()
    model.fit(X, y)
    dump(model, 'LinearRegressionModel.joblib')
    
def load_model(input_data):
    model = load('LinearRegressionModel.joblib')
    df = pd.DataFrame([input_data])
    X = df.values
    prediction = model.predict(X)
    return prediction[0]