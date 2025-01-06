import pandas as pd

class Tratamentodados:
    @staticmethod
    def tratamento(dados_json):
        df = pd.DataFrame.from_dict(dados_json, orient='index', columns=['Consumo']).reset_index()
        df.columns = ['Data', 'Consumo']
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
        return df