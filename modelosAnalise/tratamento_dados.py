import pandas as pd
import numpy as np

class Tratamentodados:
    @staticmethod
    def tratamento(dados_json):
        df = pd.DataFrame({'Data': dados_json.keys(), 'Consumo': dados_json.values()})

        for indice in df.index:
            if pd.isna(df.at[indice, 'Consumo']):
                df.at[indice, 'Consumo'] = df['Consumo'].median()

        df["Acumulado"] = [np.nan for i in range(len(df))]

        df["Acumulado"] = df['Consumo'].cumsum()

        df = df.loc[df['Consumo'] > 0.1]

        return df