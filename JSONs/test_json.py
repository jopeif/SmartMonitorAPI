import statistics as st

# with open('./Testar modelo JSON/test_json.json', 'r') as arquivo_json:
#     jsondata = json.load(arquivo_json)

valores = []
def model_json(jsondata):
    
    for i in jsondata.values():
        if i==None:
            i=0
        valores.append(i)

    for index, valor in enumerate(valores):
        if valor==None:
            mediana = st.median(valores)
            mediana = round(mediana, 5)
            valores[index] = mediana