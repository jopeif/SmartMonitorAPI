import pandas as pd

class Tratamentodados:
    @staticmethod
    def tratamento(dados_json):
        consumo = dados_json["id_sensor"]
        df = pd.DataFrame(consumo, columns=['Consumo'])
        return df