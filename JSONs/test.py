import json
import pandas as pd

with open('./Testar modelo JSON/jsondata.json', 'r') as arquivo_json:
    jsondata = json.load(arquivo_json)

jsondata_reestruturado = {}

json_prediction={

}

# Iterar pelas instituições no JSON
for instituicao, sensores in jsondata.items():
    json_prediction[instituicao] = {}
    for sensor, leituras in sensores.items():
        json_prediction[instituicao][sensor] = {}

lista1=[]
# Iterar pelas instituições no JSON
for instituicao, sensores in jsondata.items():
    jsondata_reestruturado[instituicao] = {}
    for sensor, leituras in sensores.items():
        # Criar DataFrame com os dados do sensor
        df = pd.DataFrame.from_dict(leituras, orient="index", columns=["values"])
        for data, valor in leituras.items():
            valores = list(leituras.values())
            jsondata_reestruturado[instituicao][sensor] = {}

            for data, valor in leituras.items():
                if valor is None:
                    mediana = pd.Series([v for v in valores if v is not None]).median()  
                    jsondata_reestruturado[instituicao][sensor][data] = mediana
                    lista1.append(mediana)
                else:
                    jsondata_reestruturado[instituicao][sensor][data] = valor
                    
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


# import numpy as np
# import pandas as pd
# from xgboost import XGBRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# import joblib

# for sensor in sensores:
#     keys=jsondata_reestruturado[instituicao][sensor]

#     # Extrair apenas os valores, ignorando as datas
#     values = list(keys.values())

#     modelo = joblib.load('modelosML/RandomForest/Test/test.joblib')

#     numbers_array = np.array(values).reshape(1, -1)

#     prediction = modelo.predict(numbers_array)[0]

#     prediction = float(prediction)
#     json_prediction[instituicao][sensor]=prediction














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