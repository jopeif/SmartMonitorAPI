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
        "17/11/2024": 0.45123,
    }
}

keys = list(jsondata["data"])

for i in range(len(keys)):
    date = keys[i]
    value = jsondata["data"][date]

    # Se o valor for None, pegue o valor da próxima data
    if value is None and i + 1 < len(keys):
        value = jsondata["data"][keys[i + 1]]
        print(colored(f"Data: {date}, Valor: {value}","red"))
    else:
        print(f"Data: {date}, Valor: {value}")
