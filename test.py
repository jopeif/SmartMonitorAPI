import json

jsondata={
    "data":{ 
        "11/11/2024": 0.12334,
        "12/11/2024": 0.13343,
        "13/11/2024": None,
        "14/11/2024": 0.02334,
        "15/11/2024": 0.32334,
        "16/11/2024": 0.32134,
        "17/11/2024": None,
    }
}
# import pandas as pd

# df = pd.DataFrame.from_dict(jsondata["data"], orient="index", columns=["values"])
# df["values"] = df["values"].interpolate(method="linear")
# print(df)

keys = list(jsondata["data"])

data={
    "data":{
        
    }
}

for i in range(len(keys)):
    date = keys[i]
    value = jsondata["data"][date]

    # Se o valor for None, calcule uma média dos valores anterior e sucessor, se ambos existirem.
    if value is None:
        # Pega o valor sucessor se disponível
        valueSucessor = jsondata["data"].get(keys[i + 1]) if i + 1 < len(keys) else None
        # Pega o valor anterior se disponível
        valueAnterior = jsondata["data"].get(keys[i - 1]) if i - 1 >= 0 else None

        # Calcula a média somente se ambos os valores não são None
        if valueSucessor is not None and valueAnterior is not None:
            value = (valueSucessor + valueAnterior) / 2
        elif valueAnterior is not None:
            value = valueAnterior  
        elif valueSucessor is not None:
            value = valueSucessor  

    # print(f"Data: {date}, Valor: {value:.5f}" if value is not None else f"Data: {date}, Valor: None")

    data["data"][date] = value    
print(data)