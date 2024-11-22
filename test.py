import json

jsondata={
    "Instituição 1":{
        "Sensor 1":{ 
            "11/11/2024": 0.42313,
            "12/11/2024": 0.13343,
            "13/11/2024": 0.45234,
            "14/11/2024": 0.21452,
            "15/11/2024": 0.12352,
            "16/11/2024": 0.51232,
            "17/11/2024": None,
        },
        "Sensor 2": {
            "11/11/2024": None,
            "12/11/2024": 0.34215,
        },
    },
    "Instituição 2":{
        "Sensor 21":{ 
            "18/11/2024": 1.42313,
            "19/11/2024": 0.13343,
            "20/11/2024": None,
            "21/11/2024": None,
            "22/11/2024": 2.12352,
            "23/11/2024": 3.51232,
            "24/11/2024": 0.87231,
        }
    }
}
import pandas as pd


jsondata_reestruturado = {}

# Iterar pelas instituições no JSON
for instituicao, sensores in jsondata.items():
    jsondata_reestruturado[instituicao] = {}
    for sensor, leituras in sensores.items():
        # Criar DataFrame com os dados do sensor
        df = pd.DataFrame.from_dict(leituras, orient="index", columns=["values"])
        # Preencher valores nulos com interpolação linear
        df["values"] = df["values"].interpolate(method="linear", limit_direction="both")
        # Converter de volta para dicionário
        jsondata_reestruturado[instituicao][sensor] = df["values"].to_dict()

# Agora, processar os dados interpolados
# Apenas como exemplo, usaremos a primeira instituição e sensor

for instituicao, sensores in jsondata_reestruturado.items():
    print(f"\nInstituição: {instituicao}")
    for sensor, leituras in sensores.items():
        print(f"  Sensor: {sensor}")
        for data, valor in leituras.items():
            print(f"    {data}: {valor}")












# # Novo dicionário para armazenar os dados interpolados
# jsondata_reestruturado = {}

# # Iterar pelas instituições no JSON
# for instituicao, sensores in jsondata.items():
#     jsondata_reestruturado[instituicao] = {}
#     for sensor, leituras in sensores.items():
#         # Criar DataFrame com os dados do sensor
#         df = pd.DataFrame.from_dict(leituras, orient="index", columns=["values"])
#         # Preencher valores nulos com interpolação linear
#         df["values"] = df["values"].interpolate(method="linear", limit_direction="both")
#         # Converter de volta para dicionário
#         jsondata_reestruturado[instituicao][sensor] = df["values"].to_dict()



# for i in range(0, len(jsondata_reestruturado)):

#     instituicoes = list(jsondata_reestruturado)[i]
#     print(f'\n{'-'*50}\n{instituicoes}')

#     sensores = list(jsondata_reestruturado[instituicoes].keys())
#     for sensor in sensores:
#         datas = list(jsondata_reestruturado[instituicoes][sensor].keys())
#         print(f'{sensor} : ')
#         for data in datas: 
#             consumo = jsondata_reestruturado[instituicoes][sensor][data]
#             print(f'    {data} : {consumo}')