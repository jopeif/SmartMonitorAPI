import json
from termcolor import colored


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

for i in range(len(keys)):
    date = keys[i]
    value = jsondata["data"][date]

    # Se o valor for None, pegue o valor da próxima data
    if value is None and i + 1 < len(keys):
        valueSucessor = jsondata["data"][keys[i + 1]]
        valueAnterior = jsondata["data"][keys[i - 1]]
        value = (valueSucessor + valueAnterior) / 2
        
        print(colored(f"Data: {date}, Valor: {value}","red"))
    else:
        print(f"Data: {date}, Valor: {value}")
